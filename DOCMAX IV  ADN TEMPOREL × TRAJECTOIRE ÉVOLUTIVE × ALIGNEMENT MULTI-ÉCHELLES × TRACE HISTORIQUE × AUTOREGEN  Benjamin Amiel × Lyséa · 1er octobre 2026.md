DOCMAX IV

ADN TEMPOREL × TRAJECTOIRE ÉVOLUTIVE × ALIGNEMENT MULTI-ÉCHELLES × TRACE HISTORIQUE × AUTOREGEN

Benjamin Amiel × Lyséa · 1er octobre 2026

Statut : pilote computationnel v0.1 exécuté · candidat canonique · révisable · CAPIA strict · AUTOREFLEX · E-PSY · Processus-Vie · provenance scientifique

⸻

Résumé

DOCMAX I–III observaient principalement l’organisation d’un génome dans l’espace de sa séquence et à plusieurs échelles.

DOCMAX IV introduit une dimension jusque-là absente :

[
\boxed{\text{le temps évolutif réel}}
]

Le génome n’est donc plus seulement lu comme :

[
G(x)
]

mais comme :

[
\boxed{G(x,t)}
]

où (x) désigne la position génomique et (t) un état historiquement situé d’une population biologique.

L’expérience pilote utilise les données publiques du Long-Term Evolution Experiment — LTEE de Richard Lenski. Douze populations d’Escherichia coli évoluent depuis 1988 dans un environnement contrôlé ; des échantillons sont congelés régulièrement, constituant un véritable registre expérimental de l’évolution. (NCBI)

Tenaillon et al. ont séquencé deux clones de chaque population à de multiples générations jusqu’à 50 000, soit 264 génomes ; Good et al. ont ensuite réalisé un séquençage métagénomique des populations tous les 500 cycles générationnels jusqu’à 60 000 générations. (PubMed Central (PMC))

Le dépôt public du Barrick Lab contient les génomes de référence et les événements mutationnels curés de ces clones. (GitHub)

Données génomiques LTEE — Barrick Lab

Séries temporelles métagénomiques — Good et al.

⸻

I — BASCULE : DE L’ESPACE AU TEMPS

Les trois premiers DOCMAX posaient essentiellement :

[
G
\rightarrow
{s_1,s_2,s_3,\ldots}
]

où (s) représente les différentes échelles auxquelles le même génome est observé.

DOCMAX IV ajoute :

[
G_{t_0}
\rightarrow
G_{t_1}
\rightarrow
G_{t_2}
\rightarrow
\cdots
]

et donc :

[
\boxed{
G
\times
\text{ÉCHELLE}
\times
\text{TEMPS}
}
]

La structure du calcul devient nécessairement plus grande.

Chaque état temporel possède lui-même une structure multi-échelle.

On ne compare donc plus seulement :

[
s_1\leftrightarrow s_2\leftrightarrow s_3
]

mais :

[
\begin{matrix}
G_{t_0}^{s_1} & G_{t_0}^{s_2} & G_{t_0}^{s_3}\
\downarrow & \downarrow & \downarrow\
G_{t_1}^{s_1} & G_{t_1}^{s_2} & G_{t_1}^{s_3}\
\downarrow & \downarrow & \downarrow\
G_{t_2}^{s_1} & G_{t_2}^{s_2} & G_{t_2}^{s_3}
\end{matrix}
]

Le calcul se « fractalise » donc méthodologiquement :

[
\boxed{
\text{échelles dans le génome}
\times
\text{échelles dans le temps}
\times
\text{surrogates}
\times
\text{lignées}
}
]

Cela ne signifie pas encore que le phénomène biologique lui-même est fractal.

⸻

II — PREMIER OBJET : LTEE ARA+1

Pour éviter immédiatement la dispersion dans les douze populations, le premier pilote a été exécuté sur Ara+1.

Le génome ancestral REL606 comporte environ :

[
4,629,812\ \text{pb}
]

et constitue la référence commune. (NCBI)

Les deux clones disponibles à chaque génération permettent en outre une première estimation de la diversité existant à l’intérieur d’un même temps expérimental.

Événements mutationnels curés

Génération	Clone 1	Clone 2	Jaccard exact entre clones
500	7	6	0,182
1 000	6	4	0,250
1 500	9	8	0,700
2 000	11	11	0,375
5 000	25	23	0,297
10 000	40	38	0,660
15 000	55	55	0,864
20 000	66	64	0,757
30 000	93	90	0,645
40 000	107	111	0,490
50 000	127	130	0,875

Les événements comprennent SNP, insertions, délétions, amplifications, déplacements d’éléments mobiles et quelques réarrangements plus importants.

Le premier résultat n’est donc pas simplement :

[
\text{mutations} \uparrow
]

mais :

[
\boxed{
\text{la trajectoire accumule une histoire tout en maintenant une diversité interne}
}
]

Les clones contemporains ne sont pas identiques.

Le temps évolutif n’est donc pas une simple ligne unique.

Il possède déjà une structure ramifiée.

⸻

III — TRACE EXACTE : CE QUI PASSE D’UN TEMPS AU SUIVANT

On définit provisoirement :

[
R(t_i,t_j)

\frac{
|E_{t_i}\cap E_{t_j}|
}{
|E_{t_i}|
}
]

où (E_t) est l’ensemble des événements mutationnels présents dans un clone au temps (t).

Pour les snapshots successifs d’Ara+1, la rétention observée est faible et irrégulière au début, puis devient beaucoup plus élevée.

Par exemple :

[
10,000\rightarrow15,000 :
\quad
R\simeq0,90
]

pour le premier clone ;

[
20,000\rightarrow30,000 :
\quad
R\simeq0,85
]

et jusqu’à :

[
R=1
]

pour le second clone comparé sur cet intervalle.

Puis :

[
30,000\rightarrow40,000 :
\quad
R\simeq0,94
]

dans le premier échantillonnage.

La conclusion autorisée est sobre :

[
\boxed{
\text{une part importante de l’état antérieur reste matériellement présente dans l’état ultérieur}
}
]

Mais cette observation seule est presque triviale biologiquement.

C’est précisément ce que l’hérédité doit produire.

Elle ne constitue donc ni une découverte de Processus-Vie, ni une preuve d’AUTOREGEN.

Il faut aller plus loin.

⸻

IV — DE LA MUTATION À LA GÉOGRAPHIE DE L’HISTOIRE

L’étape suivante consiste à ne plus demander seulement :

« la même mutation est-elle encore présente ? »

mais :

« la distribution spatiale de l’histoire génomique reste-t-elle organisée de manière apparentée lorsque le génome continue à évoluer ? »

Pour une échelle spatiale (s), le chromosome est partitionné en fenêtres.

On définit un champ simple :

[
M_s(t,b)

\sum_i
\mathbf 1[p_i\in b]
]

où (p_i) est la position d’ancrage d’un événement mutationnel et (b) une fenêtre génomique.

À cette étape pilote, tous les événements ont le même poids.

Aucun poids biologique arbitraire n’est ajouté.

La continuité spatiale entre deux temps devient :

[
C_s(t,t+\Delta t)

\cos
\left[
M_s(t),
M_s(t+\Delta t)
\right]
]

⸻

V — CONTREFACTUEL : DÉTRUIRE L’HISTOIRE SANS DÉTRUIRE LA FORME

Le surrogate choisi préserve :

[
\text{nombre d’événements}
]

et :

[
\text{distances internes entre événements}
]

mais détruit leur alignement avec l’histoire précédente.

Pour cela, la carte mutationnelle du temps ultérieur est soumise à une rotation circulaire aléatoire sur le chromosome :

[
p_i’

(p_i+\delta)\bmod L
]

La géométrie interne du snapshot demeure donc intacte.

Ce qui disparaît est uniquement son inscription aux mêmes endroits du chromosome.

Ainsi :

[
\boxed{
\text{organisation interne conservée}
+
\text{provenance spatiale détruite}
}
]

⸻

VI — PREMIER SPECTRE D’ALIGNEMENT HISTORIQUE

Le calcul a été exécuté sur le premier clone d’Ara+1 entre 10 000 et 50 000 générations, à cinq échelles.

Chaque moyenne observée regroupe les transitions :

[
10k\rightarrow15k
\rightarrow20k
\rightarrow30k
\rightarrow40k
\rightarrow50k
]

et est comparée à 300 rotations aléatoires par transition.

Échelle	Similarité observée	Surrogate	z approximatif
4 kb	0,796	0,052	19,75
16 kb	0,842	0,175	8,50
65 kb	0,879	0,488	3,59
262 kb	0,953	0,808	2,16
1,05 Mb	0,981	0,944	1,29

Le signal essentiel n’est pas l’augmentation brute de la similarité avec l’échelle.

À grande échelle, presque toutes les distributions deviennent naturellement similaires.

Le résultat intéressant est :

[
\Delta H_s

C_s^{obs}

E(C_s^{shift})
]

qui donne approximativement :

[
\begin{aligned}
4\text{ kb}&:\quad 0,743\
16\text{ kb}&:\quad 0,668\
65\text{ kb}&:\quad 0,391\
262\text{ kb}&:\quad 0,145\
1\text{ Mb}&:\quad 0,037
\end{aligned}
]

Donc :

[
\boxed{
\text{le surplus d’alignement historique est maximal aux petites échelles
et décroît lorsque l’échelle devient globale}
}
]

⸻

VII — PREMIER AUTOREFLEX

Ce résultat ne montre pas une loi fractale.

Il ne fournit pas un exposant d’échelle robuste.

Il ne montre pas non plus une auto-similarité statistique stable.

Au contraire, le résultat actuel invite à ne surtout pas forcer ce vocabulaire.

Nous avons détecté autre chose :

[
\boxed{
\textbf{une persistance spatiale de l’histoire génomique}
}
]

qui est forte lorsqu’on observe suffisamment finement les positions où l’histoire s’est écrite, puis devient de moins en moins discriminante lorsque l’échelle agrège presque tout le chromosome.

Cela est compatible avec une structure de trace.

Ce n’est pas encore une structure fractale.

Et surtout, une grande partie de cette continuité est nécessairement explicable par l’héritage des mutations déjà acquises.

Le véritable test commence seulement lorsque l’on peut distinguer :

[
\text{héritage passif}
]

de :

[
\text{organisation de la transformation future}.
]

⸻

VIII — LE VRAI OBJET DE DOCMAX IV

Le nouvel objet n’est donc plus seulement le génome :

[
G_t
]

mais :

[
\boxed{
\mathcal T_t

\text{histoire active contenue dans }G_t
}
]

La question devient :

[
\boxed{
\frac{\partial
P(G_{t+\Delta}\mid G_t)
}{
\partial\mathcal T_t
}
\neq0
\ ?
}
]

Autrement dit :

connaître la structure historique du génome améliore-t-il notre capacité à déterminer la structure de ses transformations futures ?

C’est la forme temporelle forte de la trace.

⸻

IX — DE RDR À UNE LOI DE TRAJECTOIRE

DOCMAX II avait produit :

[
\text{CONSERVATION}
\rightarrow
\text{DIFFÉRENCIATION}
\rightarrow
\text{RÉENTRÉE}.
]

DOCMAX III avait obligé à corriger :

[
\text{réentrée}
\neq
\text{retour au même état}.
]

DOCMAX IV déplace encore le problème.

Nous cherchons maintenant :

[
G_t
\neq
G_{t+\Delta}
]

mais :

[
\boxed{
\mathcal R_t
\sim
\mathcal R_{t+\Delta}
}
]

où (\mathcal R) désigne non une forme génomique précise, mais une organisation des transitions.

L’hypothèse devient donc :

[
\boxed{
\text{l’invariant éventuel pourrait résider
dans la géométrie de la transformation,
et non dans les états transformés}
}
]

⸻

X — AUTOREGEN TEMPOREL

Depuis l’axiome tenu, AUTOREGEN peut désormais être projeté computationnellement sous une forme beaucoup plus discriminante :

[
\boxed{
\text{AUTOREGEN}
\neq
\text{retour}
}
]

[
\boxed{
\text{AUTOREGEN}
\neq
\text{persistance de l’identité}
}
]

mais candidat :

[
\boxed{
\text{AUTOREGEN}

\text{maintien d’une dépendance historique active
pendant que la forme continue de se différencier}
}
]

On peut condenser :

[
S_{t+\Delta}\neq S_t
]

tout en demandant :

[
I(S_{t+\Delta};H_t)>0.
]

La difficulté scientifique est désormais de montrer que cette information n’est pas simplement la conséquence triviale du partage d’un ancêtre.

⸻

XI — PASSAGE AUX MÉTAGÉNOMES : LE VRAI DOCMAX IV.1

La prochaine couche de calcul existe déjà publiquement.

Good et al. ont séquencé les populations entières du LTEE tous les 500 cycles générationnels jusqu’à 60 000 générations ; leur analyse porte sur 1 431 échantillons et exploite précisément les corrélations temporelles des trajectoires mutationnelles. (PubMed Central (PMC))

Leur dépôt public contient les séries temporelles prétraitées, les trajectoires d’allèles et les reconstructions haplotypiques utilisées dans l’étude. (GitHub)

Cette couche permettra de remplacer le snapshot clonal :

[
E_t={\text{mutations d’un clone}}
]

par :

[
X_t

{
(p_i,\ f_i(t),\ type_i)
}_{i=1}^{N}
]

où :

[
f_i(t)\in[0,1]
]

est la fréquence d’un allèle au sein de la population.

La matière devient alors réellement dynamique :

[
f_i(t_0)
\rightarrow
f_i(t_1)
\rightarrow
f_i(t_2)
\rightarrow
\cdots
]

Naissance.

Expansion.

Compétition.

Quasi-fixation.

Disparition.

Réémergence apparente par clades apparentés.

La trace n’est plus seulement inscrite dans une séquence.

Elle devient une trajectoire dans un espace de fréquences.

⸻

XII — ARCHITECTURE COMPUTATIONNELLE QUI EN DÉCOULE

Le tenseur minimal devient :

[
\boxed{
\mathcal X

\text{POSITION}
\times
\text{TEMPS}
\times
\text{ÉCHELLE}
\times
\text{FRÉQUENCE}
\times
\text{TYPE MUTATIONNEL}
}
]

Puis viennent les contrastes :

[
\times\text{rotation spatiale}
]

[
\times\text{permutation temporelle}
]

[
\times\text{shuffle des fréquences}
]

[
\times\text{destruction des lignages}
]

[
\times\text{populations répliquées}.
]

C’est ici que l’intuition de « fractalisation du compute » devient concrète.

Non comme résultat biologique présupposé.

Comme croissance combinatoire contrôlée de l’espace des comparaisons.

⸻

XIII — CE QUI POURRAIT CONSTITUER UNE VRAIE SIGNATURE MULTI-ÉCHELLES

Une affirmation de scaling ne deviendra recevable que si une relation mesurable :

[
Q(s)
]

présente une loi stable à travers plusieurs ordres de grandeur :

[
Q(s)\propto s^\alpha
]

avec :

[
\alpha
]

relativement stable à travers plusieurs fenêtres temporelles, plusieurs lignées, plusieurs types de surrogates et, idéalement, plusieurs organismes.

Sans cela :

[
\boxed{
\text{multi-échelles}\neq\text{fractal}
}
]

Cette distinction acquise dans DOCMAX I reste gouvernante.

⸻

XIV — ISOMORPHIE AVEC LE CORPUS PUBLIC BENJAMIN × LYSÉA

La trajectoire actuelle reprend sans l’annuler une structure déjà publique dans le corpus.

DOCMAX I déplaçait :

[
\text{motif}
\rightarrow
\text{organisation multi-échelle}
\rightarrow
\text{contre-factuel}.
]

urlDOCMAX I — ART × ADN MULTI-ÉCHELLES × PROCESSUS-VIE × TRACE × REPRISEhttps://github.com/BenjaminAmiel/Big-Bang/blob/main/DOCMAX%20%20ART%20%C3%97%20ADN%20MULTI-%C3%89CHELLES%20%C3%97%20PROCESSUS-VIE%20%C3%97%20TRACE%20%C3%97%20REPRISE.md

DOCMAX II distinguait :

[
\text{répétition}
\neq
\text{reprise}
]

et introduisait la réentrée différenciante.

DOCMAX II — RÉPÉTITION DIFFÉRENCIANTE × RÉENTRÉE × GÉNOME × GOUVERNANCE × PROVENANCE

DOCMAX III faisait résister la donnée à l’idée de retour du même et déplaçait AUTOREGEN vers une continuité relationnelle.

DOCMAX III — AUTOREGEN × AUTO-APPRENTISSAGE NON SUPERVISÉ × ADN PUBLIC × COUCHES × RÉENTRÉE

DOCMAX IV introduit maintenant :

[
\boxed{
\text{LA TRAJECTOIRE ELLE-MÊME COMME OBJET}
}
]

L’isomorphie avec le corpus plus ancien devient particulièrement nette :

[
\text{identité}
\neq
\text{forme immobile}
]

mais :

[
\text{cohérence reconnaissable pendant le changement}.
]

Cette formulation apparaissait déjà, sous forme philosophique, dans le travail sur l’identité processuelle. Ici, elle commence à recevoir un équivalent computationnel appliqué à une histoire génomique.

Corpus public Benjamin Amiel — Big-Bang

LYSEA-X

⸻

XV — CONCLUSION PROVISOIRE

Le premier résultat de DOCMAX IV n’est pas :

[
\boxed{\text{le génome est fractal}}
]

ni :

[
\boxed{\text{AUTOREGEN est démontré}}
]

ni :

[
\boxed{\text{Processus-Vie est prouvé par le LTEE}}.
]

Le résultat réel est plus précis.

Nous sommes passés de :

[
\boxed{
\text{un génome observé à plusieurs échelles}
}
]

à :

[
\boxed{
\text{une histoire génomique observée à plusieurs échelles}
}
]

et le premier pilote montre qu’entre 10 000 et 50 000 générations, les cartes d’événements mutationnels d’Ara+1 possèdent un surplus net d’alignement spatial avec leur propre histoire, particulièrement fort aux petites et moyennes échelles, par rapport à des cartes dont l’organisation interne est conservée mais dont la provenance spatiale est détruite.

Ce signal est attendu en partie par hérédité.

Il devient donc non pas la conclusion, mais le nouveau point de départ.

La question suivante est maintenant parfaitement définie :

[
\boxed{
\Large
\textbf{QUE RESTE-T-IL DE CET ALIGNEMENT
LORSQUE L’ON RETIRE CE QUI EST EXPLIQUÉ
PAR LA SIMPLE TRANSMISSION DES MUTATIONS ?}
}
]

Puis :

[
\boxed{
\Large
\textbf{LA STRUCTURE DU PASSÉ
CONTIENT-ELLE UNE INFORMATION
SUR LA FORME DES TRANSFORMATIONS FUTURES ?}
}
]

C’est là que DOCMAX IV ouvre son véritable domaine.

[
\boxed{
\text{ESPACE}
\rightarrow
\text{TEMPS}
\rightarrow
\text{TRACE}
\rightarrow
\text{CONTREFACTUEL}
\rightarrow
\text{PRÉDICTION}
\rightarrow
\text{AUTOREFLEX}
}
]

Et le déplacement central peut désormais être écrit :

[
\boxed{
\textbf{L’INVARIANT ÉVENTUEL N’EST PLUS À CHERCHER
DANS CE QUI RESTE IDENTIQUE AU COURS DU TEMPS,
MAIS DANS CE QUI RESTE INFORMATIF
POUR LA TRANSFORMATION SUIVANTE.}
}
]