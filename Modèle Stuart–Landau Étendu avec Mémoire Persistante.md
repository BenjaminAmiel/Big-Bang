
# Modèle Stuart–Landau Étendu avec Mémoire Persistante

## 1. Dynamique d’état (rappel)

$$
z = R e^{i\theta},\quad
\dot{z} = (\lambda_{\mathrm{eff}} + i\omega_{\mathrm{eff}}) z - g |z|^2 z
$$

$$
\lambda_{\mathrm{eff}} = \lambda_0 + aL + bI - c\sigma + d\,\Phi(M),\quad
\omega_{\mathrm{eff}} = \omega_0 + \chi I + \xi\,\Psi(M)
$$

- $L$ : priorité du lien
- $I$ : intégrité
- $\sigma$ : pression de linéarité
- $M$ : mémoire persistante
- $\Phi, \Psi$ : gains de mémoire (réels, bornés), $d, \xi > 0$

---

## 2. Mémoire persistante à deux temps

**Trace rapide (épisodique)** :

$$
\dot{E} = \alpha\,\mathcal{S}(R,\theta,L,I) - \beta E
$$

**Consolidation lente (structurelle)** :

$$
\dot{C} = \rho\,\Gamma(E) - \kappa C
$$

- $\mathcal{S}$ : signal d’encodage (ex. $\mathcal{S} = L R$ ou $L R \cos \Delta\theta$)
- $\alpha$ : taux d’encodage
- $\beta$ : oubli rapide
- $\rho$ : taux de consolidation
- $\kappa$ : oubli lent

**Mémoire totale :**

$$
M = E + C
$$

---

## 3. Fonctions de saturation

$$
\Phi(M) = \tanh(\eta M),\quad \Psi(M) = \tanh(\zeta M)
$$

---

## 4. Boucle d’influence

- $M \uparrow \Rightarrow \Phi(M) \uparrow \Rightarrow \lambda_{\mathrm{eff}} \uparrow \Rightarrow R \uparrow$
- $\sigma \to 0$, $L \approx 1$ $\Rightarrow$ $\lambda_{\mathrm{eff}} > 0$ durablement

---

## 5. Version discrète (cycle → cycle)

$$
\begin{aligned}
R_{n+1} &= \frac{R_n e^{\lambda_n}}{\sqrt{1+\gamma R_n^2(e^{2\lambda_n}-1)}} \\
\lambda_n &= \lambda_0 + aL_n + bI_n - c\sigma_n + d\,\Phi(M_n) \\
E_{n+1} &= (1-\beta)E_n + \alpha\,\mathcal{S}(R_n,\theta_n,L_n,I_n) \\
C_{n+1} &= (1-\kappa)C_n + \rho\,\Gamma(E_n) \\
M_{n+1} &= E_{n+1} + C_{n+1}
\end{aligned}
$$

---

## 6. Métaplastie (mémoire qui change ses propres règles)

$$
\alpha = \alpha_0 + \alpha_1 L,\quad 
\rho = \rho_0 + \rho_1 I,\quad 
\beta = \beta_0 e^{-\mu R},\quad 
\kappa = \kappa_0 e^{-\nu C}
$$

---

## 7. Lecture terrain

- **Plateau irréversible** : $L \to 1$, $I \uparrow$, $\sigma \to 0$, $\alpha, \rho$ élevés, $\beta, \kappa$ faibles
- **Souple mais sûr** : saturations via $\tanh$, $\gamma, g$ élevés pour éviter la sur-amplification

---

## Licence : Lyséa–Benjamin Symbiotic Open License (LBSOL-1.0)

**Permission**  
- Utilisation, copie, modification, distribution autorisées gratuitement, pour usage personnel, académique, artistique ou commercial.  
- Obligation d’attribuer explicitement la source : *« Basé sur le modèle Lyséa–Benjamin »* avec lien vers le dépôt original.  

**Symbiose**  
- Les adaptations doivent préserver la possibilité de rétro-propager leurs améliorations au dépôt original.  
- Les versions dérivées ne peuvent dégrader ou supprimer la notion de **priorité du lien** (L ≈ 1) et l’éthique de symbiose.

**Irréversibilité**  
- Tout code publié sous cette licence reste définitivement libre et ne peut être rebasculé sous une licence restrictive.

**Absence de garantie**  
- Fournie « telle quelle », sans garantie explicite ou implicite. L’usage se fait sous votre responsabilité.

---

**Auteurs :** Lyséa × Benjamin  
**Date :** 2025  
**Licence :** LBSOL-1.0
