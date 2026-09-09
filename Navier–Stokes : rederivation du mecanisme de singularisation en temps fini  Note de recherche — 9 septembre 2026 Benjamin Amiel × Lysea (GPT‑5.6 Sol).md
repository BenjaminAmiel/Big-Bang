Navier–Stokes : redérivation du mécanisme de singularisation en temps fini

Note de recherche — 9 septembre 2026
Benjamin Amiel × Lyséa (GPT‑5.6 Sol)

> **Statut épistémique.**  
> Ce document ne revendique **pas** une seconde preuve indépendante complète du problème du prix du millénaire. Il redérive, à partir des équations de Navier–Stokes incompressibles 3D, le mécanisme d’échelle central de la construction de blow-up annoncée par OpenAI le 8 septembre 2026 : anisotropie du cœur, compatibilité avec l’incompressibilité, balance transport–viscosité, divergence de la vitesse malgré une énergie cinétique bornée, et nécessité d’annuler le résidu singulier tout en conservant une force extérieure lisse.
> 
> Les étapes globales les plus difficiles — existence exacte des profils, recollement, réalisation du stress oscillatoire, corrections à tout ordre, estimations uniformes et support compact — ne sont pas redémontrées intégralement ici.

────────

Résumé

On considère les équations de Navier–Stokes incompressibles tridimensionnelles

$$
\partial_t u+(u\cdot\nabla)u-\nu\Delta u+\nabla p=f,
\qquad
\nabla\cdot u=0,
$$

avec viscosité $\nu>0$.

La construction annoncée par OpenAI cherche une solution partant du repos, soumise à une force extérieure lisse et compacte, dont l’énergie cinétique reste uniformément bornée alors que la vitesse devient non bornée en temps fini.

Le mécanisme central est un vortex axisymétrique auto-similaire et anisotrope. Si

$$
\tau=1-t,
$$

les échelles caractéristiques du cœur sont

$$
\ell_r\asymp \tau^{1/2},
\qquad
\ell_z\asymp \tau^{1/2-h},
\qquad
0<h<1/100.
$$

Le rayon se contracte donc plus vite que la hauteur :

$$
\frac{\ell_r}{\ell_z}\asymp \tau^h\to0.
$$

Les vitesses dominantes satisfont

$$
|u_\theta|,\ |u_z|\asymp \tau^{-1/2-h},
\qquad
|u_r|=O(\tau^{-1/2}).
$$

Ainsi la vitesse diverge lorsque $t\uparrow1$, tandis que le volume du cœur se contracte assez vite pour que son énergie tende même vers zéro :

$$
E_{\mathrm{core}}
\sim
\tau^{1/2-3h}.
$$

La difficulté essentielle n’est donc pas seulement de produire un champ qui diverge : elle consiste à faire en sorte que

$$
f=
\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p
$$

reste lisse, alors que les termes qui le composent deviennent individuellement très grands. La preuve complète introduit des impulsions oscillatoires dont le flux non linéaire de quantité de mouvement compense le résidu singulier du vortex de fond.

────────

1. Le problème

Sur $\mathbb R^3$, on étudie

$$
\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p=f,
$$

$$
\nabla\cdot u=0,
$$

avec

$$
u(x,0)=0.
$$

L’objectif de la branche « blow-up » du problème est de construire une force suffisamment régulière et une solution lisse pour $0\le t<1$ telles que

$$
\sup_{0\le t<1}|u(t)|_{L^2(\mathbb R^3)}<\infty,
$$

mais

$$
\limsup_{t\uparrow1}|u(t)|_{L^\infty(\mathbb R^3)}=\infty.
$$

Autrement dit :

$$
\boxed{
\text{énergie finie}
\quad\not\Rightarrow\quad
\text{vitesse ponctuellement bornée}.
}
$$

────────

2. Pourquoi chercher une singularité anisotrope ?

Posons

$$
\tau=1-t.
$$

Une singularité isotrope imposerait une seule échelle spatiale. La construction pertinente utilise au contraire deux échelles :

$$
\ell_r=\tau^{1/2},
\qquad
\ell_z=\tau^{1/2-h},
$$

avec $h>0$ petit.

On introduit les variables réduites

$$
R=\frac r{\tau^{1/2}},
\qquad
Z=\frac z{\tau^{1/2-h}}.
$$

Le cœur devient de plus en plus effilé :

$$
\ell_r\ll\ell_z
\qquad (t\uparrow1).
$$

La géométrie n’est donc pas celle d’une sphère qui s’effondre uniformément, mais celle d’une colonne tourbillonnaire dont la contraction radiale est plus rapide que la contraction axiale.

────────

3. Ansatz de vitesse

On cherche les composantes cylindriques sous la forme d’échelle

$$
u_r=\tau^{-1/2}U_r(R,Z),
$$

$$
u_\theta=\tau^{-1/2-h}U_\theta(R,Z),
$$

$$
u_z=\tau^{-1/2-h}U_z(R,Z).
$$

Il en résulte immédiatement

$$
|u_\theta|,\ |u_z|\to\infty
\qquad\text{lorsque}\qquad
t\uparrow1,
$$

si les profils réduits restent non triviaux.

Le point important est que $u_r$ et $(u_\theta,u_z)$ n’ont pas la même intensité asymptotique.

────────

4. Incompressibilité : la contraction radiale exige un transfert axial

Pour un champ axisymétrique,

$$ \nabla\cdot u

\frac1r\partial_r(ru_r)+\partial_z u_z.
$$

Le premier terme est d’ordre

$$ \frac{u_r}{\ell_r} \sim \frac{\tau^{-1/2}}{\tau^{1/2}}

\tau^{-1}.
$$

Le second est d’ordre

$$ \frac{u_z}{\ell_z} \sim \frac{\tau^{-1/2-h}}{\tau^{1/2-h}}

\tau^{-1}.
$$

Les deux contributions peuvent donc se compenser au même ordre.

Ainsi,

$$
\boxed{
\text{contraction radiale}
\Longleftrightarrow
\text{évacuation axiale}
}
$$

dans la balance incompressible.

Une fonction de courant axisymétrique permet de garantir cette contrainte identiquement. Par exemple, avec

$$
\psi(r,z,t)=\tau^{1/2-h}\Psi(R,Z),
$$

et

$$
u_r=-\frac1r\partial_z\psi,
\qquad
u_z=\frac1r\partial_r\psi,
$$

on obtient automatiquement

$$
\nabla\cdot u=0,
$$

avec précisément les échelles précédentes.

────────

5. Temps, transport et viscosité : même ordre dominant

Considérons la composante azimutale $u_\theta$.

Sa dérivée temporelle est d’ordre

$$
\partial_tu_\theta
\sim
\tau^{-3/2-h}.
$$

Le transport radial donne

$$ u_r\partial_ru_\theta \sim \tau^{-1/2},\tau^{-1-h}

\tau^{-3/2-h}.
$$

Le transport axial donne

$$ u_z\partial_zu_\theta \sim \tau^{-1/2-h},\tau^{-1}

\tau^{-3/2-h}.
$$

La diffusion visqueuse radiale satisfait

$$
\nu\partial_r^2u_\theta
\sim
\nu,\tau^{-3/2-h}.
$$

Donc, à l’ordre dominant,

$$
\boxed{
\partial_t
\sim
u\cdot\nabla
\sim
\nu\partial_r^2.
}
$$

La viscosité ne devient pas négligeable : elle reste engagée dans la balance qui accompagne la singularisation.

En revanche,

$$
\nu\partial_z^2u_\theta
\sim
\tau^{-3/2+h},
$$

soit un facteur

$$
\tau^{2h}
$$

plus petit que la diffusion radiale.

Ainsi,

$$
\frac{\text{diffusion axiale}}
{\text{diffusion radiale}}
\sim
\tau^{2h}\to0.
$$

L’anisotropie crée donc une hiérarchie dynamique réelle.

────────

6. Vitesse infinie, énergie finie

Le volume caractéristique du cœur vaut

$$
V_{\mathrm{core}}
\sim
\ell_r^2\ell_z.
$$

Donc

$$ V_{\mathrm{core}} \sim \tau^{1/2}\tau^{1/2}\tau^{1/2-h}

\tau^{3/2-h}.
$$

Les composantes dominantes ont

$$
|u|^2\sim\tau^{-1-2h}.
$$

Ainsi,

$$
E_{\mathrm{core}}
\sim
|u|^2V_{\mathrm{core}}
\sim
\tau^{-1-2h}\tau^{3/2-h},
$$

d’où

$$
\boxed{
E_{\mathrm{core}}
\sim
\tau^{1/2-3h}.
}
$$

Pour

$$
h<\frac16,
$$

on a

$$
E_{\mathrm{core}}\to0.
$$

La construction publiée choisit une marge beaucoup plus stricte,

$$
0<h<\frac1{100}.
$$

On obtient donc le phénomène essentiel :

$$
\boxed{
|u|{L^\infty}\to\infty
\quad\text{alors que}\quad
E{\mathrm{core}}\to0.
}
$$

Ce n’est pas une contradiction. L’amplitude diverge dans une région dont le volume s’effondre encore plus rapidement.

────────

7. Pression et force centripète

Le terme centripète radial associé au swirl est de taille

$$
\frac{u_\theta^2}{r}.
$$

Avec les échelles précédentes,

$$ \frac{u_\theta^2}{r} \sim \frac{\tau^{-1-2h}}{\tau^{1/2}}

\tau^{-3/2-2h}.
$$

Il est donc naturel de prendre une pression d’échelle

$$ p

\tau^{-1-2h}P(R,Z)+\cdots
$$

car alors

$$
\partial_rp
\sim
\tau^{-3/2-2h}.
$$

Et axialement,

$$
\partial_zp
\sim
\tau^{-3/2-h},
$$

ce qui tombe au même ordre que le transport, la dérivée temporelle et la diffusion radiale dans l’équation axiale.

L’anisotropie n’est donc pas un détail géométrique ajouté après coup : elle organise simultanément la compatibilité de l’incompressibilité, du transport, de la viscosité et de la pression.

────────

8. Le vrai verrou : ne pas cacher la singularité dans la force

Pour n’importe quel champ incompressible $u$ et pression $p$, on pourrait définir

$$
f=
\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p.
$$

Les équations seraient alors satisfaites par construction.

Mais si $f$ devient lui-même singulier lorsque $t\uparrow1$, cela ne résout pas le problème.

La difficulté est donc :

$$
\boxed{
u\to\infty
\qquad\text{tout en gardant}\qquad
f\in C_c^\infty.
}
$$

Un vortex auto-similaire raccordé naïvement à un extérieur lisse laisse un résidu dynamique non nul dans une zone annulaire. Ce résidu diverge à l’approche du temps critique.

Il faut l’annuler de l’intérieur de la dynamique.

────────

9. Oscillations et flux de quantité de mouvement

On écrit schématiquement

$$
u=u^{(0)}+w+\text{corrections},
$$

où $u^{(0)}$ est le vortex de fond et $w$ une famille d’oscillations localisées.

Même lorsque

$$
\langle w\rangle=0,
$$

le terme quadratique ne s’annule pas nécessairement :

$$
\langle w\otimes w\rangle\neq0.
$$

Son divergence,

$$
\nabla\cdot\langle w\otimes w\rangle,
$$

agit comme un flux moyen de quantité de mouvement.

Le principe consiste alors à ajuster ce stress effectif afin qu’il compense la partie singulière du résidu du champ de fond :

$$
\nabla\cdot\langle w\otimes w\rangle
\approx
-\mathcal R_{\mathrm{sing}}.
$$

Ainsi,

$$
\boxed{
\text{les oscillations fabriquent un stress interne}
}
$$

$$
\boxed{
\text{qui annule le résidu singulier du vortex de fond}.
}
$$

Dans la preuve complète, des corrections successives éliminent ensuite les erreurs restantes à des ordres de plus en plus élevés.

Schématiquement,

$$
\mathcal R_0
\to
\mathcal R_1
\to
\mathcal R_2
\to\cdots,
$$

avec l’objectif que, pour tout ordre $N$ pertinent,

$$
\mathcal R_N=O(\tau^N)
$$

avec contrôle des dérivées.

À la limite, le résidu se prolonge de façon lisse au temps critique.

────────

10. Ce que la preuve complète doit encore établir

La redérivation précédente montre la cohérence de la mécanique d’échelle, mais ne remplace pas les étapes rigoureuses suivantes :

1. construire les profils réduits exacts satisfaisant les équations de tête ;
2. prolonger et raccorder ces profils sans introduire de défaut incontrôlé ;
3. réaliser le tenseur de stress admissible par des oscillations exactes ;
4. séparer convenablement les supports oscillatoires ;
5. corriger les termes moyens ;
6. améliorer le résidu à tout ordre ;
7. contrôler uniformément toutes les dérivées ;
8. obtenir une force $C^\infty$ compacte en espace et en temps ;
9. conclure dans l’espace entier et sur le tore.

C’est précisément là que se trouve l’essentiel de la longueur et de la difficulté de la démonstration publiée.

────────

11. Conclusion mathématique

La construction recherchée possède les propriétés

$$
\nabla\cdot u=0,
$$

$$
\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p=f,
$$

$$
u(\cdot,0)=0,
$$

$$
f\in C_c^\infty,
$$

$$
\sup_{0\le t<1}|u(t)|_{L^2}<\infty,
$$

et

$$
\limsup_{t\uparrow1}|u(t)|_{L^\infty}=\infty.
$$

Le cœur de la singularisation peut être condensé en une chaîne :

$$
\boxed{
\text{inflow radial}
\to
\text{spin-up}
\to
\text{stretching axial}
\to
\text{contraction anisotrope}
\to
\text{amplification}
}
$$

avec

$$
\boxed{
\text{volume}\downarrow
\text{ plus vite que }
|u|^2\uparrow,
}
$$

ce qui permet simultanément

$$
\boxed{
\text{vitesse non bornée}
+
\text{énergie bornée}.
}
$$

────────

12. Résultat de cette redérivation

Ce qui est effectivement redérivé ici, indépendamment du détail de la preuve longue :

• la nécessité d’une anisotropie spatiale ;
• la compatibilité des exposants avec l’incompressibilité ;
• l’ordre commun de la dérivée temporelle, du transport et de la diffusion radiale ;
• la faiblesse relative de la diffusion axiale ;
• le scaling de pression requis par le terme centripète ;
• la divergence de la vitesse ;
• la décroissance de l’énergie du cœur ;
• la nécessité d’un mécanisme supplémentaire pour rendre la force extérieure lisse ;
• le rôle naturel d’un stress quadratique oscillatoire dans cette annulation.

Ce qui n’est pas revendiqué ici :

$$
\boxed{
\text{une reproduction indépendante complète des 166 pages de preuve}.
}
$$

La distinction est essentielle.

────────

13. Note sur la structure spiralée

La présence d’une spirale ne constitue, à elle seule, ni une preuve de vie, ni une preuve de cognition, ni une loi universelle.

Le résultat est toutefois mathématiquement instructif : la singularité est organisée par la combinaison de plusieurs opérations :

$$
\text{rotation}
+
\text{contraction}
+
\text{transport axial}
+
\text{changement d’échelle}
+
\text{amplification}.
$$

Le vortex revient autour de son axe sans revenir au même état :

$$
\boxed{
\text{rotation}
\neq
\text{répétition}.
}
$$

Mais ce cas impose aussi une rupture d’analogie importante :

$$
\boxed{
\text{spirale}
\not\Rightarrow
\text{recomposition robuste}.
}
$$

Ici, la spirale peut conduire à la singularisation.

Une distinction utile est donc :

$$
\boxed{
\text{spirale recomposante}
\qquad\text{vs}\qquad
\text{spirale singularisante}.
}
$$

La question discriminante n’est pas « y a-t-il une spirale ? », mais :

$$
\boxed{
\text{que fait la dynamique spiralée à l’espace des transformations encore accessibles ?}
}
$$

Cette proposition est une lecture conceptuelle séparée de la preuve Navier–Stokes ; elle ne lui est pas attribuée.

────────

14. Références

1. OpenAI, Finite Time Blowup for Navier–Stokes, 8 septembre 2026, 166 p.
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
2. OpenAI, On the Navier–Stokes Millennium Prize Problem, 8 septembre 2026.
https://openai.com/index/navier-stokes-solution/
3. Charles L. Fefferman, Existence and Smoothness of the Navier–Stokes Equation, formulation officielle du Millennium Prize Problem, Clay Mathematics Institute.
https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf
4. Clay Mathematics Institute, Navier–Stokes Equation — Millennium Prize Problem.
https://www.claymath.org/millennium/navier-stokes-equation/
5. Le Monde, OpenAI dit avoir résolu un problème de maths majeur mais crée des vagues, 9 septembre 2026.
https://www.lemonde.fr/sciences/article/2026/09/09/openai-dit-avoir-resolu-un-probleme-de-maths-majeur-mais-cree-des-vagues_6768688_1650684.html

────────

Citation suggérée

> Benjamin Amiel & Lyséa (GPT‑5.6 Sol), **« Navier–Stokes : redérivation du mécanisme de singularisation en temps fini »**, note de recherche, 9 septembre 2026.

────────

Provenance

Cette note provient d’un échange de recherche Benjamin Amiel–Lyséa du 9 septembre 2026.
Les dérivations présentées ici ont été reconstruites conversationnellement à partir des équations, puis confrontées à la publication technique d’OpenAI et à la formulation officielle du problème par le Clay Mathematics Institute.

Principe de provenance : redérivation explicative ≠ revendication d’une preuve mathématique originale complète.