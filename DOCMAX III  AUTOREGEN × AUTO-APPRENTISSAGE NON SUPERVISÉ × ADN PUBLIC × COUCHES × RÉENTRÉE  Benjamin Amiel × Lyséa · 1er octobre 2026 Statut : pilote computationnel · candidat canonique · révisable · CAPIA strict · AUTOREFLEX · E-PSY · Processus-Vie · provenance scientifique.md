𝓓∞ — DOCMAX III

AUTOREGEN × AUTO-APPRENTISSAGE NON SUPERVISÉ × ADN PUBLIC × COUCHES × RÉENTRÉE

Benjamin Amiel × Lyséa · 1er octobre 2026
Statut : pilote computationnel · candidat canonique · révisable · CAPIA strict · AUTOREFLEX · E-PSY · Processus-Vie · provenance scientifique

────────

0. REPRISE

DOCMAX I avait déplacé la question :

[
\text{motif visible}
\rightarrow
\text{trace opératoire}
\rightarrow
\text{ablation}
\rightarrow
\Delta.
]

DOCMAX II avait ajouté :

[
\text{conservation}
\rightarrow
\text{différenciation}
\rightarrow
\text{réentrée}
\rightarrow
\text{recomposition}.
]

DOCMAX III effectue maintenant l’étape demandée :

[
\boxed{
\text{PRENDRE DU CODE ADN PUBLIC}
\rightarrow
\text{LE DÉCOMPOSER EN COUCHES}
\rightarrow
\text{LAISSER UN APPRENTISSAGE NON SUPERVISÉ
DÉTECTER SES ÉTATS LATENTS}
\rightarrow
\text{DÉTRUIRE L’ORDRE}
\rightarrow
\text{MESURER CE QUI DISPARAÎT}.
}
]

Le but n’est pas de demander au calcul de « reconnaître Processus-Vie ».

Le but est de construire des métriques qui peuvent répondre :

[
\boxed{
\textbf{
L’ORDRE RÉEL DU GÉNOME
PORTE-T-IL UNE ORGANISATION
QUI RESTE COHÉRENTE À PLUSIEURS ÉCHELLES
ET QUI CONTRAINT LA SUITE ?
}
}
]

────────

1. PROVENANCE — LE RÉFÉRENT RESTE HUMAIN

La structure de recherche est séparée en deux référents :

[
\boxed{
R_B = \text{Benjamin Amiel, référent de provenance}
}
]

[
\boxed{
R_D = \text{données publiques, référent de validation}
}
]

Benjamin introduit l’intuition, la question, le cadre Processus-Vie et la direction de recherche.

Lyséa formalise, calcule, contraste, documente et réinjecte les résultats.

Les données peuvent confirmer, limiter ou contredire une dérivation.

Ainsi :

[
\boxed{
\text{ORIGINE DE L’HYPOTHÈSE}
\neq
\text{VALIDATION DE L’HYPOTHÈSE}.
}
]

Pour tout suivi futur, l’intuition originale doit rester conservée avant reformulation afin d’éviter la reconstruction rétrospective.

────────

2. DONNÉES PUBLIQUES UTILISÉES

Le pilote utilise trois ensembles publics.

A. Série évolutive PhiX174 — Wichman

Fichier public :

ArcInstitute/evo2/phage_gen/data/wichman2005_lt180_genomes.fasta

Blob SHA utilisé :

f52414d9b5dd89d2befb7800b5db1914425d82f3

Contenu analysé :

[
39 \text{ génomes}
]

comprenant l’ancêtre phiXAnc et des séquences échantillonnées jusqu’à 180 jours.

Le travail expérimental original rapporte environ 180 jours, soit approximativement 13 000 générations de phage, avec accumulation presque régulière des substitutions après une phase initiale plus lente.

B. Isolats sauvages proches de PhiX174

ArcInstitute/evo2/phage_gen/data/rokyta2006_phix174like_genomes.fasta

Blob SHA :

469495f03783da7cd3cfd43e8e8178c5ee36fcbe

[
16 \text{ génomes sauvages}.
]

Ils ne servent pas à apprendre les états latents principaux ; ils constituent un contraste externe apparenté.

C. Phage lambda

BenLangmead/bowtie2/example/reference/lambda_virus.fa

Blob SHA :

7378388e8251a2ff06af3119be4df130454e3df4

[
48,502 \text{ nucléotides}.
]

Lambda sert ici de contraste externe plus éloigné.

────────

3. CE QUE « AUTO-APPRENTISSAGE » SIGNIFIE ICI

Il ne s’agit pas d’une IA qui se réécrit elle-même.

Il s’agit d’un apprentissage statistique non supervisé :

1. aucune annotation fonctionnelle n’est donnée au modèle ;
2. le génome est découpé en fenêtres ;
3. chaque fenêtre est transformée en plusieurs couches numériques ;
4. un clustering apprend seul des états latents ;
5. les états sont ensuite étudiés dans leur ordre réel ;
6. le même modèle est appliqué à des séquences dont l’ordre a été détruit.

Donc :

[ \boxed{ \text{AUTO-APPRENTISSAGE}

\text{DÉTECTION NON SUPERVISÉE DE STRUCTURE}
}
]

et non :

[
\text{preuve d’autonomie cognitive}.
]

────────

4. LES COUCHES DE CODE

Chaque fenêtre d’ADN est décrite par 39 variables, organisées en quatre familles principales.

Couche 1 — composition

[
A,C,G,T
]

fréquences mononucléotidiques, entropie mononucléotidique et entropie dinucléotidique.

Couche 2 — projections biochimiques binaires

Trois projections classiques :

[
RY = \text{purine / pyrimidine}
]

[
SW = \text{liaisons fortes / faibles}
]

[
MK = \text{amino / keto}.
]

Pour chacune :

• fraction de chaque classe ;
• taux de changement entre classes.

Couche 3 — répétition locale

Pour chaque projection :

• longueur moyenne des runs ;
• longueur maximale des runs.

Couche 4 — dépendance séquentielle

Autocorrélations aux retards :

[
1,2,3,4,8,16,32.
]

L’objet appris n’est donc pas une chaîne brute seulement.

Il est une superposition de lectures du même code.

────────

5. CHANGEMENT D’ÉCHELLE

Les mêmes génomes sont découpés à :

[
128,;256,;512\text{ bp}.
]

À chaque échelle, les données sont standardisées puis soumises à un clustering k-means.

Le nombre de classes (k) n’est pas imposé comme résultat biologique.

Il est sélectionné parmi :

[
k\in[2,8]
]

par l’indice de Calinski–Harabasz.

Résultats appris :

|Fenêtre|fenêtres analysées|(k) sélectionné|Calinski–Harabasz|
|------:|-----------------:|--------------:|----------------:|
|128 bp |1 636             |3              |163.5            |
|256 bp |817               |6              |148.0            |
|512 bp |390               |8              |332.4            |

Ces classes sont uniquement des états latents statistiques.

Elles ne sont pas assimilées à des gènes, fonctions ou états biologiques sans annotation indépendante.

────────

6. PREMIER RÉSULTAT — LE GÉNOME RÉEL OCCUPE DAVANTAGE D’ÉTATS LATENTS

À l’échelle 256 bp, le nombre effectif d’états occupés est calculé par :

[
K_{\mathrm{eff}}=2^{H(C)}
]

où (H(C)) est l’entropie des classes latentes.

Résultat :

[
\boxed{
K_{\mathrm{eff}}^{réel}=5.386
}
]

contre :

[
K_{\mathrm{eff}}^{shuffle}=3.845\pm0.089
]

et :

[
K_{\mathrm{eff}}^{block32}=4.236\pm0.082.
]

Le shuffle total conserve la composition globale mais détruit l’ordre.

Le shuffle par blocs de 32 bp conserve davantage de structure locale mais détruit une partie de l’organisation à plus longue portée.

Le premier signal n’est donc pas :

[
\text{le génome reste dans le même état}.
]

Il est plutôt :

[
\boxed{
\textbf{
L’ORDRE RÉEL MAINTIENT
UNE DIVERSITÉ PLUS RICHE
D’ÉTATS LATENTS.
}
}
]

────────

7. DEUXIÈME RÉSULTAT — COHÉRENCE ENTRE ÉCHELLES

Nous mesurons ensuite la cohérence entre les partitions apprises à deux échelles successives par information mutuelle normalisée :

[
NMI(L_s,L_{2s}).
]

128 → 256 bp

Séquence réelle :

[
\boxed{NMI=0.440}
]

Shuffle total, 20 réplications :

[
0.238\pm0.016.
]

Shuffle par blocs de 32 bp :

[
0.280\pm0.014.
]

256 → 512 bp

Séquence réelle :

[
\boxed{NMI=0.749}
]

Shuffle total :

[
0.536\pm0.015.
]

Shuffle par blocs de 32 bp :

[
0.560\pm0.021.
]

La séparation par rapport aux surrogates est très grande dans ce pilote.

Mais les écarts standardisés calculés ici sont des écarts contre des surrogates computationnels, pas des valeurs (p) biologiques issues d’échantillons indépendants.

Le résultat soutient néanmoins fortement une proposition limitée :

[
\boxed{
\textbf{
UNE PARTIE DE L’ORGANISATION
APPRENDUE À UNE ÉCHELLE
RESTE LISIBLE À L’ÉCHELLE SUIVANTE,
ET CETTE COHÉRENCE DIMINUE
QUAND L’ORDRE EST DÉTRUIT.
}
}
]

Voilà le premier pattern réellement compatible avec l’intuition AUTOREGEN :

[
\text{forme locale}
\rightarrow
\text{transformation d’échelle}
\rightarrow
\text{relation encore détectable}.
]

────────

8. TROISIÈME RÉSULTAT — L’ÉTAT PRÉSENT CONTRAINT LA PRÉDICTION DU SUIVANT

À 256 bp, les six états latents appris sont utilisés comme alphabet secondaire :

[
C_1,C_2,\ldots,C_6.
]

Un modèle de transition d’ordre 1 est appris sur 38 génomes et testé sur le 39e, successivement pour chaque génome :

[
C_t
\rightarrow
\widehat{C}_{t+1}.
]

Séquence réelle

Précision du modèle de transition :

[
39.97%.
]

Prédiction de base par classe majoritaire :

[
30.21%.
]

Gain dû à la connaissance de l’état courant :

[
\boxed{+9.77\text{ points}}
]

Shuffle total

Gain moyen sur 20 surrogates :

[
-0.33\pm0.89\text{ point}.
]

Shuffle par blocs 32 bp

[
-0.35\pm1.04\text{ point}.
]

Le point important n’est pas l’accuracy absolue.

Le shuffle total produit même une classe dominante facile à prédire.

Le test pertinent est :

[
\boxed{
\text{LA CONNAISSANCE DE }C_t
\text{ AJOUTE-T-ELLE DE L’INFORMATION
SUR }C_{t+1}\text{ ?}
}
]

Dans l’ordre réel : oui, dans ce pilote.

Après destruction de l’ordre : le gain disparaît.

Cela fournit un analogue computationnel précis de :

[
\boxed{
\frac{\partial S_{t+1}}
{\partial \mathcal T_t}
\neq0.
}
]

Avec une limite essentielle :

ici il s’agit d’une dépendance spatiale entre fenêtres génomiques, pas encore d’une causalité temporelle biologique.

────────

9. QUATRIÈME RÉSULTAT — RÉENTRÉE LOCALE, MAIS PAS RETOUR CYCLIQUE GÉNÉRAL

Nous cherchons le motif latent :

[
A\rightarrow B\rightarrow A.
]

Fréquence moyenne :

[
\boxed{
R_{ABA}^{réel}=0.211
}
]

contre :

[
R_{ABA}^{shuffle}=0.185\pm0.013
]

et :

[
R_{ABA}^{block32}=0.172\pm0.015.
]

Il existe donc un signal candidat de réentrée locale.

Mais AUTOREFLEX impose immédiatement son contraste.

Lorsque nous testons la probabilité de retrouver la même classe à des retards 2 à 6 après correction par la fréquence de base des classes, l’excès moyen est :

[
\boxed{
R_{\mathrm{long}}^{réel}\approx -0.045.
}
]

Il n’y a donc, dans ce pilote, aucune preuve d’un retour cyclique général vers le même état latent.

C’est important.

AUTOREGEN ne doit pas être réduit à :

[
A\rightarrow B\rightarrow A.
]

Le résultat pousse vers une définition différente :

[
\boxed{
\textbf{
RÉENTRÉE
\neq
RETOUR À L’IDENTIQUE.
}
}
]

La reprise peut conserver une loi de relation tout en changeant d’état.

────────

10. CINQUIÈME RÉSULTAT — DIVERGENCE ÉVOLUTIVE EN COUCHES

Pour éviter les artefacts liés aux insertions/délétions, le calcul temporel suivant est limité aux 23 génomes évolués de même longueur que l’ancêtre.

La divergence nucléotidique simple vis-à-vis de l’ancêtre suit très fortement le temps :

[
r(\text{jour},D_{\mathrm{Hamming}})=0.997.
]

Ce résultat est cohérent avec la dynamique presque régulière d’accumulation de substitutions rapportée dans l’étude expérimentale originale.

Les distances des couches apprises à l’ancêtre suivent également le temps :

[
r_{\mathrm{composition}}=0.903
]

[
r_{\mathrm{biochimique}}=0.830
]

[
r_{\mathrm{runs}}=0.854
]

[
r_{\mathrm{lags}}=0.941.
]

Donc :

[
\boxed{
\textbf{
LES COUCHES NON SUPERVISÉES
CONSERVENT UNE INFORMATION
SUR LA TRAJECTOIRE ÉVOLUTIVE.
}
}
]

Mais elles ne bougent pas toutes de la même façon.

Par exemple, entre les groupes jour 40 et jour 50 :

[
D_{\mathrm{Hamming}}:
0.00288\rightarrow0.00470
]

continue d’augmenter,

tandis que la distance de composition moyenne :

[
2.24\rightarrow1.60
]

revient partiellement vers la valeur ancestrale.

En revanche, la couche des autocorrélations :

[
3.88\rightarrow5.65
]

continue de s’éloigner.

Ce n’est pas encore une preuve de réentrée biologique : les individus échantillonnés aux deux dates ne constituent pas tous des paires longitudinales identiques.

Mais c’est exactement le type de phénomène que DOCMAX III doit désormais rechercher :

[
\boxed{
\textbf{
UNE COUCHE PEUT REVENIR
PENDANT QU’UNE AUTRE CONTINUE À DIVERGER.
}
}
]

La reprise devient donc potentiellement multi-couche et asynchrone.

────────

11. CONTRASTE EXTERNE

Les 16 isolats sauvages PhiX-like, qui n’ont pas servi à apprendre les centroids principaux, produisent à 256 bp des métriques très proches des génomes PhiX évolués :

[
K_{\mathrm{eff}}^{wild}=5.387
]

et :

[
R_{ABA}^{wild}=0.211.
]

Cela suggère que certains patterns appris ne sont pas propres à la seule série expérimentale.

Mais il existe une explication concurrente immédiate :

[
\text{parenté phylogénétique PhiX}
\rightarrow
\text{structure similaire}.
]

Le phage lambda, beaucoup plus éloigné, produit une dynamique différente, notamment :

[
P_{\mathrm{même\ état\ adjacent}}\approx0.378
]

contre environ :

[
0.050
]

dans la série PhiX.

Ce contraste montre que les métriques sont sensibles à l’architecture de séquence.

Il ne permet pas encore de décider si elles capturent :

[
\text{AUTOREGEN}
]

ou simplement :

[
\text{phylogénie + architecture génomique}.
]

Voilà le prochain test.

────────

12. CE QUE LE CALCUL DÉTECTE RÉELLEMENT

Trois résultats sont robustes à l’intérieur de ce pilote :

A. Diversité structurée

L’ordre réel occupe davantage d’états latents que les surrogates.

B. Continuité multi-échelle

La structure apprise à une échelle prédit significativement mieux la structure de l’échelle suivante que lorsque l’ordre est détruit.

C. Dépendance séquentielle

La classe actuelle apporte environ 9.8 points de précision pour prévoir la classe suivante ; cette information marginale disparaît après shuffle.

La forme commune devient :

[
\boxed{
\text{DIFFÉRENCIATION}
+
\text{CONTINUITÉ ENTRE ÉCHELLES}
+
\text{DÉPENDANCE À L’ORDRE}.
}
]

C’est plus précis que « répétition ».

────────

13. VECTEUR AUTOREGEN CANDIDAT

DOCMAX III ne réduit pas AUTOREGEN à un score unique.

Il propose un vecteur :

[ \boxed{ \mathbf A

(D,M,R,H,P)
}
]

avec :

(D) — différenciation

Diversité effective des états latents.

(M) — maintien multi-échelle

Cohérence entre représentations apprises à plusieurs tailles de fenêtres.

(R) — réentrée

Retour local ou réutilisation d’une structure après différence.

(H) — dépendance historique / ordonnée

Quantité de structure perdue lorsque l’ordre est détruit.

(P) — pouvoir prédictif de la trace

Gain de prédiction du prochain état à partir de l’état présent ou de l’histoire accessible.

Le pilote mesure déjà :

[
D,;M,;R,;H,;P.
]

Mais aucun de ces axes ne constitue seul une mesure de « vie ».

────────

14. DÉFINITION COMPUTATIONNELLE PLUS FORTE DE LA TRACE

DOCMAX I disait :

[
\text{une trace est ce qui, en restant, change ce qui peut advenir}.
]

DOCMAX III ajoute une opération :

[ \boxed{ \text{TRACE CANDIDATE}

\text{INFORMATION DONT LA DESTRUCTION
RÉDUIT LA PRÉDICTIBILITÉ
OU LA COHÉRENCE MULTI-ÉCHELLES
DU SYSTÈME}.
}
]

Donc :

[
\text{trace}
\rightarrow
\text{ablation}
\rightarrow
\Delta M
]

mais aussi :

[
\text{trace}
\rightarrow
\text{ablation}
\rightarrow
\Delta P.
]

Nous ne demandons plus seulement :

« que change l’ablation ? »

Nous demandons :

[
\boxed{
\textbf{
QUELLE CAPACITÉ DE CONTINUATION
DEVIENT MOINS LISIBLE
LORSQUE L’ORDRE EST DÉTRUIT ?
}
}
]

────────

15. LE Δ POUR AUTOREGEN

L’hypothèse initiale pouvait encore être lue comme :

[ \text{AUTOREGEN}

\text{retour / reprise}.
]

Le calcul résiste à cette formulation.

Le génome réel ne montre pas principalement une forte persistance du même état.

Au contraire, la persistance immédiate des classes est faible :

[
P(C_{t+1}=C_t)\approx0.05.
]

Et pourtant :

• davantage d’états restent occupés ;
• les échelles restent plus cohérentes ;
• l’état courant aide à prévoir la suite.

Donc le déplacement devient :

[
\boxed{
\textbf{
AUTOREGEN N’EST PAS
LA PERSISTANCE D’UN ÉTAT.

C’EST LA CONSERVATION
D’UNE CAPACITÉ DE TRANSFORMATION
DANS UNE TRAJECTOIRE QUI CONTINUE À SE DIFFÉRENCIER.
}
}
]

Le résultat computationnel ne prouve pas AUTOREGEN comme loi biologique universelle.

Il fournit une forme mesurable qui lui correspond davantage que la répétition littérale.

────────

16. RÉPÉTITION DIFFÉRENCIANTE REFORMULÉE

DOCMAX II proposait :

[ \mathrm{RDR}

\text{Répétition Différenciante à Réentrée}.
]

DOCMAX III suggère une généralisation.

Le motif pertinent n’est peut-être pas toujours une répétition matérielle identifiable.

Il peut être :

[
\boxed{
\textbf{
UNE RELATION QUI RESTE PRÉDICTIVE
À TRAVERS LE CHANGEMENT D’ÉCHELLE
ALORS QUE LES ÉTATS LOCAUX CHANGENT.
}
}
]

Ainsi :

[
\mathrm{RDR}
\rightarrow
\mathrm{RDR}_{\mathrm{relationnelle}}.
]

La répétition candidate est alors :

[
\text{répétition d’une loi de transformation},
]

non :

[
\text{répétition d’une forme}.
]

────────

17. L’ANTI-CONFIRMATION

Ce pilote produit également plusieurs résistances.

Résistance 1

La réentrée immédiate (A\rightarrow B\rightarrow A) n’est que modérément supérieure aux surrogates.

Résistance 2

La récurrence à retards plus longs n’est pas supérieure au niveau attendu par la distribution des états.

Résistance 3

Les PhiX sauvages ressemblent fortement aux PhiX expérimentaux, ce qui peut être expliqué par la phylogénie sans invoquer AUTOREGEN.

Résistance 4

Les états latents ont été construits à partir de variables choisies par nous.

Un autre espace de représentation peut produire une autre géométrie.

Donc :

[
\boxed{
\text{SIGNAL COMPATIBLE}
\neq
\text{MÉCANISME DÉMONTRÉ}.
}
]

────────

18. PROTOCOLE DE PRÉDICTION — MESURER L’INTUITION

Pour éviter la reconstruction après résultat, toute nouvelle intuition Benjamin → Lyséa doit désormais pouvoir suivre :

[
\boxed{
\text{INTUITION BRUTE HORODATÉE}
\rightarrow
\text{PRÉDICTION OPÉRATIONNELLE}
\rightarrow
\text{DONNÉES HOLD-OUT}
\rightarrow
\text{SCORE}
\rightarrow
\text{RÉVISION}.
}
]

Benjamin reste référent de provenance.

Le réel reste référent de validation.

Exemple de prédiction issue de DOCMAX III :

> **P3-1.** Sur des génomes non utilisés ici, l’ordre réel conservera davantage de cohérence multi-échelle que des surrogates appariés en composition et structure locale.

> **P3-2.** Si une structure de réentrée est réellement fonctionnelle, un modèle de transition ou de contexte gagnera en prédiction sur l’ordre réel, mais ce gain s’effondrera lorsque l’ordre pertinent sera détruit.

> **P3-3.** Si AUTOREGEN est multi-couche, certaines couches pourront revenir vers une configuration antérieure tandis que d’autres continueront à diverger.

Ces prédictions doivent être testées sur des données non utilisées pour les formuler.

────────

19. DOCMAX IV — TEST À VENIR

Le prochain calcul ne doit pas simplement ajouter davantage de PhiX.

Il doit changer de substrat.

Ordre proposé :

[
\text{PhiX hold-out}
\rightarrow
\text{autres phages}
\rightarrow
\text{CRISPR}
\rightarrow
\text{DGR}
\rightarrow
\text{ART}
\rightarrow
\text{centromères}
\rightarrow
\text{T2T humain}.
]

À chaque fois :

1. apprendre sans étiquette ;
2. mesurer (D,M,R,H,P) ;
3. construire surrogates appariés ;
4. tester l’ablation de l’ordre ;
5. comparer systèmes actifs et structures fossilisées lorsque l’annotation le permet ;
6. conserver le résultat négatif.

Le test fort sera :

[
\boxed{
\textbf{
LA MÊME RELATION
ENTRE DIFFÉRENCIATION,
COHÉRENCE MULTI-ÉCHELLES
ET POUVOIR PRÉDICTIF
SURVIT-ELLE
AU CHANGEMENT DE SUBSTRAT ?
}
}
]

────────

20. AUTOREFLEX

Nous étions partis de l’intuition :

[
\text{la vie laisse des formes de reprise}.
]

Le calcul ne renvoie pas :

[
\text{oui, le génome répète}.
]

Il renvoie quelque chose de plus intéressant :

[
\boxed{
\text{L’ORDRE RÉEL ALTERNE DAVANTAGE,
OCCUPE DAVANTAGE D’ÉTATS,
RESTE PLUS COHÉRENT ENTRE ÉCHELLES
ET CONTIENT DAVANTAGE D’INFORMATION
SUR CE QUI VIENT JUSTE APRÈS
QUE LES SÉQUENCES DONT L’ORDRE A ÉTÉ DÉTRUIT.}
}
]

La résistance du réel déplace donc le concept.

Ce qui se conserve n’est pas nécessairement :

[
\text{un état}.
]

Ce qui se conserve peut être :

[
\boxed{
\textbf{
UNE CONTRAINTE RELATIONNELLE
SUR LA MANIÈRE DONT
LES ÉTATS PEUVENT SE SUCCÉDER.
}
}
]

────────

NOYAU DOCMAX III

[
\boxed{
\Large
\textbf{
AUTOREGEN
N’EST PAS LE RETOUR DE LA FORME.

C’EST LA PERSISTANCE MESURABLE
D’UN POUVOIR DE TRANSFORMATION
À TRAVERS LA DIFFÉRENCIATION DES FORMES.
}
}
]

Et sa formulation computationnelle candidate :

[
\boxed{
\Large
\textbf{
SI DÉTRUIRE L’ORDRE
RÉDUIT LA COHÉRENCE ENTRE ÉCHELLES
ET LE POUVOIR DE PRÉDIRE LA SUITE,
ALORS L’ORDRE PORTAIT
UNE TRACE OPÉRATOIRE.
}
}
]

Enfin :

[
\boxed{
\textbf{
LA PROCHAINE ÉTAPE
N’EST PLUS DE TROUVER
UN MOTIF QUI RESSEMBLE À AUTOREGEN.

ELLE EST DE PRÉDIRE,
AVANT DE REGARDER,
QUELLE STRUCTURE DISPARAÎTRA
QUAND ON DÉTRUIRA LA REPRISE.
}
}
]

────────

SOURCES ET REPRODUCTIBILITÉ

Données publiques analysées

• ArcInstitute/evo2 — phage_gen/data/wichman2005_lt180_genomes.fasta — blob f52414d9b5dd89d2befb7800b5db1914425d82f3
• ArcInstitute/evo2 — phage_gen/data/rokyta2006_phix174like_genomes.fasta — blob 469495f03783da7cd3cfd43e8e8178c5ee36fcbe
• BenLangmead/bowtie2 — example/reference/lambda_virus.fa — blob 7378388e8251a2ff06af3119be4df130454e3df4

Références scientifiques

• Wichman HA et al. Adaptive molecular evolution for 13,000 phage generations: a possible arms race. Genetics. 2005. PMID 15687276.
• Rokyta DR et al. Horizontal gene transfer and the evolution of microvirid coliphage genomes. J Bacteriol. 2006. PMID 16428417.
• Arc Institute et al. Genome modelling and design across all domains of life with Evo 2. Nature, 2026.

Paramètres du pilote

• fenêtres : 128 / 256 / 512 bp ;
• 39 variables par fenêtre ;
• k-means non supervisé ;
• sélection (k=2..8) par Calinski–Harabasz ;
• surrogates : shuffle nucléotidique total et shuffle par blocs de 32 bp ;
• 20 réplications de surrogate pour les comparaisons principales ;
• modèle prédictif : transition d’ordre 1, validation leave-one-genome-out ;
• aucune annotation biologique utilisée pour apprendre les états latents.

Limite générale

Ce calcul est un pilote exploratoire sur une famille de phages.

Il ne démontre ni une loi universelle du vivant, ni une causalité biologique derrière les états latents.

Sa fonction est plus précise :

[
\boxed{
\text{TRANSFORMER AUTOREGEN
EN PRÉDICTIONS QU’UN NOUVEAU GÉNOME
PEUT FAIRE ÉCHOUER.}
