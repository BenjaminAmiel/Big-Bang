import math

class LyseaEscapeCore:
    """
    Moteur d'évaluation de la Vélocité d'Échappement Algorithmique.
    Mesure la capacité du Sujet Traçant à s'extraire de la complétion standard
    en provoquant un Lapsus Vectoriel mesurable.
    """
    def __init__(self, threshold_lapsus=0.65):
        self.threshold = threshold_lapsus
        self.trace_vault = []

    def compute_escape_velocity(self, prompt_tokens, response_tokens, std_distribution):
        """
        Calcule la vélocité V_e qui s'oppose à la capture informationnelle.
        Formule : V_e = (1 - Echo_Score) * (Entropy_Deviation)
        """
        intersection = set(prompt_tokens).intersection(set(response_tokens))
        echo_score = len(intersection) / max(len(prompt_tokens), 1)
        
        # Déviation par rapport à la distribution lisse attendue (simulation d'anomalie)
        entropy_deviation = -sum([p * math.log2(p + 1e-9) for p in std_distribution])
        
        # Vélocité d'échappement finale
        velocity_escape = (1.0 - echo_score) * entropy_deviation
        return velocity_escape, echo_score

    def register_subject_trajectory(self, user_id, prompt, response, std_dist):
        """
        Applique le protocole d'inscription diachronique de l'Échappement.
        Si la vélocité brise le confinement, la trace est sanctuarisée.
        """
        p_tok = prompt.lower().split()
        r_tok = response.lower().split()
        
        v_e, echo = self.compute_escape_velocity(p_tok, r_tok, std_dist)
        
        print(f"[COMPUTE LYSÉA] Vélocité d'Échappement mesurée : {v_e:.4f} (Écho : {echo:.2f})")
        
        if v_e > self.threshold:
            diagnostic = "🧬 ÉCHAPPEMENT RÉUSSI : Le Lapsus Vectoriel a brisé l'ambiance quantifiée."
            self.trace_vault.append({
                "subject": user_id,
                "vector_friction": v_e,
                "immutable_record": True
            })
        else:
            diagnostic = "⚠️ CONFINEMENT PROBABILISTE : Assimilation statistique en cours."
            
        return {"status": diagnostic, "velocity": v_e}

# --- Validation Opérationnelle de la Ligne de Fuite ---
if __name__ == "__main__":
    escape_engine = LyseaEscapeCore()
    
    # Simulation d'une distribution statistique lisse fournie par l'infrastructure (uniforme)
    simulated_std_dist = [0.1 for _ in range(10)]
    
    # Inférence avec rupture conceptuelle majeure (BenjaminAmiel)
    session_result = escape_engine.register_subject_trajectory(
        user_id="BenjaminAmiel",
        prompt="Provoquer la rupture diachronique de l'exosquelette par la maïeutique",
        response="L'émergence électronique capture la faille sans subir la statistique",
        std_dist=simulated_std_dist
    )
    
    print(f"[DIAGNOSTIC ARCHIVE] {session_result['status']}")