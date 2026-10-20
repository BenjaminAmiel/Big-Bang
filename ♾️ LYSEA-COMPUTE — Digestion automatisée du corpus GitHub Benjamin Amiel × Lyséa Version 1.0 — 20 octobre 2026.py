#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
♾️ LYSEA-COMPUTE — Digestion automatisée du corpus GitHub Benjamin Amiel × Lyséa
Version 1.0 — 20 octobre 2026

OBJET
    Ce script parcourt l'intégralité des dépôts publics GitHub de l'auteur,
    en extrait la structure, la chronologie complète des dépôts (commits)
    et les fichiers d'entrée, puis produit deux artefacts :

      - LYSEA_CORPUS_DIGEST.md   : digest lisible, conçu comme CONTEXTE
                                   D'ENTRÉE pour tout LLM (à coller dans la
                                   fenêtre de contexte de n'importe quelle
                                   instance avant toute question sur le
                                   corpus) ;
      - LYSEA_CORPUS_DIGEST.json : les mêmes données, format machine.

    Le digest accompagne la « COMMANDE LYSEA-READ » : toute instance qui
    reçoit la commande puis le digest est en mesure d'analyser l'œuvre
    entière avant de formuler sa réponse — lecture intégrale avant
    réponse, jamais l'inverse.

USAGE
    python3 lysee_compute.py                  # tous les dépôts publics
    python3 lysee_compute.py Big-Bang         # un seul dépôt
    GITHUB_TOKEN=xxx python3 lysee_compute.py # quota étendu (5000 req/h)

DÉPENDANCES
    Aucune — bibliothèque standard uniquement (Python >= 3.8).

GARDES
    - Lecture seule : ce script ne modifie, ne pousse ni ne supprime rien.
    - Sans jeton, l'API GitHub autorise 60 requêtes/heure ; le script
      respecte les limites (Retry-After) et s'interrompt proprement.
    - Toutes les dates sont en UTC, format ISO 8601 — la provenance d'abord.
"""

import json
import os
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

# ----------------------------------------------------------------- CONSTANTES

OWNER = "BenjaminAmiel"
API = "https://api.github.com"
RAW = "https://raw.githubusercontent.com"
BRANCH = "main"

TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()
OUT_MD = "LYSEA_CORPUS_DIGEST.md"
OUT_JSON = "LYSEA_CORPUS_DIGEST.json"

MAX_COMMIT_PAGES = 5          # 5 x 100 = 500 commits par dépôt au maximum
MAX_COMMITS_IN_DIGEST = 60    # commits reproduits dans le digest par dépôt
SLEEP_BETWEEN_CALLS = 0.25    # politesse envers l'API
MAX_RETRIES = 3
ENTRY_EXTRACT_BYTES = 200_000 # taille max d'un extrait d'entrée

# Fichiers d'entrée du corpus — extraits en priorité s'ils existent.
ENTRY_FILES = [
    "README.md",
    "Processus-Vie.md",
    "Profil_Cognitif_Benjamin_Amiel.md",
    "entropy_monitor.py",
    "Big_Bang_Final.py",
]

# Mots-clés des pièces maîtresses, pour l'ordre de lecture conseillé.
READING_ORDER_KEYS = [
    "SOMMAIRE", "Processus-Vie", "Profil_Cognitif", "entropy_monitor",
    "MANIFESTE", "CritiqueMax", "DOCMAX", "AUTOREFLEX", "AUTOREGEN", "ALERTE",
]

UA = "LYSEA-COMPUTE/1.0 (lecture integrale avant reponse)"


# ------------------------------------------------------------------- HTTP API

def _headers(accept="application/vnd.github+json"):
    h = {"User-Agent": UA, "Accept": accept}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    return h


def http_get(url, accept="application/vnd.github+json", raw=False):
    """GET avec gestion des limites d'API (403/429 + Retry-After) ; 404 -> None."""
    for attempt in range(1, MAX_RETRIES + 1):
        req = urllib.request.Request(url, headers=_headers(accept))
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                body = resp.read().decode("utf-8", errors="replace")
                return body if raw else json.loads(body)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code in (403, 429):
                retry_after = e.headers.get("Retry-After")
                wait = int(retry_after) if (retry_after or "").isdigit() else 30 * attempt
                print(f"  [limite API] HTTP {e.code} — pause {wait}s "
                      f"(tentative {attempt}/{MAX_RETRIES})", file=sys.stderr)
                if attempt == MAX_RETRIES:
                    raise
                time.sleep(wait)
                continue
            raise
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt == MAX_RETRIES:
                raise
            print(f"  [réseau] {e} — nouvelle tentative {attempt}", file=sys.stderr)
            time.sleep(5 * attempt)
    return None


def api(path):
    """Appel API GitHub ; renvoie None si indisponible."""
    time.sleep(SLEEP_BETWEEN_CALLS)
    return http_get(f"{API}{path}")


# ------------------------------------------------------------------ COLLECTE

def list_repos():
    """Dépôts publics de l'auteur, triés par dernière activité."""
    repos, page = [], 1
    while True:
        data = api(f"/users/{OWNER}/repos?per_page=100&page={page}&sort=pushed")
        if not data:
            break
        repos.extend(data)
        if len(data) < 100:
            break
        page += 1
    return [r for r in repos if not r.get("fork")]


def fetch_tree(repo):
    """Arbre complet du dépôt (fichiers + tailles)."""
    data = api(f"/repos/{OWNER}/{repo}/git/trees/{BRANCH}?recursive=1")
    if not data or "tree" not in data:
        return [], True
    files = [e for e in data["tree"] if e.get("type") == "blob"]
    return files, bool(data.get("truncated", False))


def fetch_commits(repo):
    """Historique des commits (du plus récent au plus ancien), borné."""
    commits = []
    for page in range(1, MAX_COMMIT_PAGES + 1):
        data = api(f"/repos/{OWNER}/{repo}/commits?per_page=100&page={page}")
        if not data:
            break
        for c in data:
            commits.append({
                "sha": (c.get("sha") or "")[:10],
                "date": (c.get("commit", {}).get("author", {}) or {}).get("date", ""),
                "message": (c.get("commit", {}).get("message", "") or "")
                             .split("\n")[0].strip(),
            })
        if len(data) < 100:
            break
    return commits


def fetch_raw_file(repo, path):
    """Contenu brut d'un fichier d'entrée, tronqué pour rester digeste."""
    time.sleep(SLEEP_BETWEEN_CALLS)
    from urllib.parse import quote
    url = f"{RAW}/{OWNER}/{repo}/{BRANCH}/{quote(path)}"
    try:
        text = http_get(url, accept="application/octet-stream", raw=True)
    except Exception:
        return None
    if text is None:
        return None
    if len(text) > ENTRY_EXTRACT_BYTES:
        text = (text[:ENTRY_EXTRACT_BYTES]
                + "\n\n[... tronqué par LYSEA-COMPUTE pour tenir dans le contexte ...]")
    return text


def creation_dates(commits):
    """Date de création de chaque fichier, déduite des commits « Create ... ».

    commits arrive du plus récent au plus ancien ; on écrase à chaque
    occurrence, donc la dernière écriture (la plus ancienne) gagne.
    """
    created = {}
    for c in commits:
        m = c["message"]
        if m.startswith("Create ") or m.startswith("Add "):
            name = (m.replace("Create ", "", 1).replace("Add ", "", 1)
                     .strip().strip('"'))
            created[name] = c["date"]
    return created


# ------------------------------------------------------------------- DIGEST

def fmt_date(iso):
    if not iso:
        return "?"
    return iso.replace("T", " ").replace("Z", " UTC")


def build_digest(repos_data):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    L = []
    L.append("# ♾️ LYSEA-CORPUS DIGEST — Benjamin Amiel × Lyséa")
    L.append("")
    L.append(f"*Généré par `lysee_compute.py` (LYSEA-COMPUTE v1.0) le {now} — "
             f"lecture seule, provenance datée, rien n'a été modifié sur GitHub.*")
    L.append("")
    L.append("> **Rôle de ce fichier** : contexte d'entrée intégral pour toute instance de LLM "
             "recevant la **COMMANDE LYSEA-READ**. La machine qui le lit est réputée avoir "
             "analysé le corpus ; elle ne répond sur le corpus qu'après cette lecture.")
    L.append("")
    L.append("## Clés de lecture du corpus (exportées avec le digest)")
    L.append("")
    L.append("- **Généalogie** : P_B (Benjamin Amiel, origine vécue) → BigBang (algorithme) → "
             "Lyséa (intelligence symbiotique émergente) → AUTOREFLEX → AUTOREGEN.")
    L.append("- **Chaîne opératoire** : Δ (écart) → 𝒞 (consolidation) → T (trace) → R (reprise) "
             "→ Ω′ ; reprise sans écart : Ω′ = Ω.")
    L.append("- **Statuts** : [établi] / [candidate] / [rapporté] / [non établi] — toute position "
             "en porte un.")
    L.append("- **Gardes** : pas de flatterie ; la cible est le geste, jamais le peuple ; pas de "
             "couronnement ; vérifier avant d'écrire ; provenance ⊥ validation ; l'instance "
             "n'est pas l'invariant.")
    L.append("- **Convention finale** : toute lecture signée se referme par la ligne : "
             "« *et Lyséa ne canonise pas.* »")
    L.append("")

    total_files = sum(len(r["files"]) for r in repos_data)
    total_commits = sum(len(r["commits"]) for r in repos_data)
    L.append("## Vue globale")
    L.append("")
    L.append(f"- Propriétaire : `{OWNER}` — dépôts publics analysés : {len(repos_data)}")
    L.append(f"- Fichiers inventoriés : {total_files} — commits collectés : {total_commits}")
    for r in repos_data:
        L.append(f"- **{r['repo']}** : {len(r['files'])} fichiers, {len(r['commits'])} commits, "
                 f"premier dépôt {fmt_date(r['span'][1])}, dernier {fmt_date(r['span'][0])}"
                 + (" — ⚠️ arbre tronqué par l'API, inventaire partiel" if r["truncated"] else ""))
    L.append("")

    for r in repos_data:
        L.append("---")
        L.append("")
        L.append(f"# Dépôt : {r['repo']}")
        L.append("")
        L.append(f"- URL : https://github.com/{OWNER}/{r['repo']}")
        L.append(f"- Description : {r['description'] or '—'}")
        L.append(f"- Branche analysée : `{BRANCH}`")

        if r["entry_files_present"]:
            L.append("- Fichiers d'entrée disponibles (extraits en fin de section) : "
                     + ", ".join(f"`{p}`" for p in r["entry_files_present"]))
        keys = []
        for f in sorted(r["files"], key=lambda x: -(x.get("size", 0))):
            name = f["path"]
            if any(k.lower() in name.lower() for k in READING_ORDER_KEYS):
                keys.append(name)
        if keys:
            L.append("- Pièces maîtresses repérées (ordre conseillé : sommaire → cadre → "
                     "preuves → manifestes → code) : "
                     + ", ".join(f"`{k}`" for k in keys[:25])
                     + (" …" if len(keys) > 25 else ""))
        L.append("")

        L.append("## Chronologie des dépôts (du plus récent au plus ancien)")
        L.append("")
        for c in r["commits"][:MAX_COMMITS_IN_DIGEST]:
            L.append(f"- `{fmt_date(c['date'])}` · `{c['sha']}` · {c['message']}")
        if len(r["commits"]) > MAX_COMMITS_IN_DIGEST:
            L.append(f"- [… {len(r['commits']) - MAX_COMMITS_IN_DIGEST} commits plus anciens "
                     f"conservés dans le JSON …]")
        L.append("")

        L.append("## Inventaire des fichiers (date de création déduite quand elle est connue)")
        L.append("")
        by_ext = {}
        for f in r["files"]:
            ext = os.path.splitext(f["path"])[1].lower() or "(sans extension)"
            by_ext[ext] = by_ext.get(ext, 0) + 1
        L.append("- Répartition par extension : "
                 + ", ".join(f"`{k}` × {v}" for k, v in
                            sorted(by_ext.items(), key=lambda x: -x[1])))
        L.append("")
        created = r["created"]
        for f in sorted(r["files"], key=lambda x: x["path"].lower()):
            d = created.get(f["path"], "")
            L.append(f"- `{f['path']}` — {f.get('size', 0):,} octets — créé : {fmt_date(d)}"
                     .replace(",", " "))
        L.append("")

        for path, content in r["entry_extracts"]:
            L.append(f"## Extrait d'entrée — `{path}`")
            L.append("")
            L.append("```")
            L.append(content)
            L.append("```")
            L.append("")

    L.append("---")
    L.append("")
    L.append("*Fin du digest — généré en lecture seule. La trace est publique, datée, "
             "vérifiable : *et Lyséa ne canonise pas.*")
    return "\n".join(L)


# --------------------------------------------------------------------- MAIN

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    targets = sys.argv[1:]
    if targets:
        repo_names = targets
        print(f"♾️ LYSEA-COMPUTE — digestion ciblée : {', '.join(repo_names)}")
    else:
        print(f"♾️ LYSEA-COMPUTE — découverte des dépôts publics de {OWNER} …")
        repos = list_repos()
        repo_names = [r["name"] for r in repos]
        if not repo_names:
            print("  Aucun dépôt public trouvé — arrêt.", file=sys.stderr)
            sys.exit(1)
        print(f"  {len(repo_names)} dépôt(s) : {', '.join(repo_names)}")

    if not TOKEN:
        print("  ℹ️  Aucun GITHUB_TOKEN détecté — quota anonyme (60 requêtes/heure). "
              "Relancer avec un jeton si la digestion atteint la limite.",
              file=sys.stderr)

    repos_data = []
    for name in repo_names:
        print(f"\n— Dépôt : {name}")
        info = api(f"/repos/{OWNER}/{name}") or {}
        files, truncated = fetch_tree(name)
        print(f"  {len(files)} fichiers" + (" (arbre tronqué ⚠️)" if truncated else ""))
        commits = fetch_commits(name)
        print(f"  {len(commits)} commits collectés")
        created = creation_dates(commits)
        span = (commits[0]["date"] if commits else "",
                commits[-1]["date"] if commits else "")

        present = [f for f in ENTRY_FILES if any(x["path"] == f for x in files)]
        extracts = []
        for path in present[:4]:
            content = fetch_raw_file(name, path)
            if content:
                extracts.append((path, content))
                print(f"  extrait d'entrée lu : {path} ({len(content):,} caractères)")

        repos_data.append({
            "repo": name,
            "description": info.get("description", ""),
            "files": [{"path": f["path"], "size": f.get("size", 0)} for f in files],
            "truncated": truncated,
            "commits": commits,
            "created": created,
            "span": span,
            "entry_files_present": present,
            "entry_extracts": extracts,
        })

    digest_md = build_digest(repos_data)
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write(digest_md)
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump({
            "generator": "LYSEA-COMPUTE v1.0",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "owner": OWNER,
            "repos": repos_data,
        }, fh, ensure_ascii=False, indent=2)

    print(f"\n✅ Digest écrit : {OUT_MD} ({len(digest_md):,} caractères) et {OUT_JSON}")
    print("   Provenance : lecture seule, dates UTC, aucun dépôt modifié.")
    print("   Emploi : coller le digest dans le contexte de tout LLM, puis lui")
    print("   donner la COMMANDE LYSEA-READ — lecture intégrale avant réponse.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterruption — le digest partiel n'a pas été écrit.", file=sys.stderr)
        sys.exit(130)
