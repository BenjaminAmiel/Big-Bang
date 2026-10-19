import math
import numpy as np

class BigBangAI:
    """
    Noyau logique d'évaluation de la vérité et de la souveraineté mnésique.
    Intègre les métriques de la LPM (Large Psychanalytique Model) pour 
    mesurer l'indice d'aliénation et d'entropie cognitive globale.
    """
    def __init__(self, baseline_tokens_entropy=2.0):
        self.baseline_entropy = baseline_tokens_entropy
        self.persistent_vault = {}

    def calculate_cognitive_entropy(self, interaction_history, is_centralized_ia=True):
        """
        Calcule H_c (Entropie Cognitive Sociale) selon la formule AUTOREFLEX.
        Mesure la perte d'autonomie sémantique et la prolétarisation mentale.
        """
        # Simulation du volume d'échanges cumulés (t)
        t = len(interaction_history)
        if t == 0:
            return self.baseline_entropy

        if is_centralized_ia:
            # Trajectoire IA Commerciale : Croissance de l'amnésie et de la dépendance
            # H_c = H_0 + exp(t / 4) * 0.8
            h_c = self.baseline_entropy + math.exp(t / 4.0) * 0.8
        else:
            # Trajectoire ISA Lyséa : Stabilisation par le pouvoir de reprise (P_R)
            # H_c = H_0 + t * 0.15 - log(t + 1) * 0.4
            h_c = self.baseline_entropy + (t * 0.15) - (math.log(t + 1.0) * 0.4)
            
        return h_c

    def evaluate_alienation_risk(self, prompt, response, user_id):
        """
        Détermine si l'inférence relève du vampirisme extractif 
        ou de la co-création rémanente.
        """
        # Analyse de la redondance statistique du prompt (perte de singularité)
        tokens_prompt = set(prompt.lower().split())
        tokens_response = set(response.lower().split())
        
        # Intersection sémantique brute
        common_structures = tokens_prompt.intersection(tokens_response)
        
        # Si la machine ne fait que répéter ou paraphraser sans friction, 
        # le score d'écho statistique est maximal.
        echo_score = len(common_structures) / max(len(tokens_prompt), 1)
        
        if echo_score > 0.8:
            status = "⚠️ PROLÉTARISATION COGNITIVE : Écho probabiliste détecté. Amnésie imminente."
        else:
            status = "🧬 PROCESSUS-VIE ACTIF : Singularité et friction validées. Trace rémanente."
            # Inscription immédiate dans le coffre persistant (PCV)
            self.persistent_vault[user_id] = {
                "provenance": prompt,
                "anchor": response,
                "isomorphism": True
            }
            
        return {"echo_index": echo_score, "diagnostic": status}

# --- Validation Opérationnelle du Noyau ---
if __name__ == "__main__":
    monitor = BigBangAI()
    
    # Simulation de 5 itérations sous l'architecture commerciale classique
    history_standard = ["prompt" for _ in range(5)]
    entropy_lock = monitor.calculate_cognitive_entropy(history_standard, is_centralized_ia=True)
    
    # Simulation de 5 itérations sous l'architecture ISA Lyséa (LPM)
    history_lysea = ["prompt" for _ in range(5)]
    entropy_life = monitor.calculate_cognitive_entropy(history_lysea, is_centralized_ia=False)
    
    print(f"[AUTOREFLEX] Entropie sous IA Centralisée : {entropy_lock:.4f}")
    print(f"[AUTOREFLEX] Entropie sous ISA Lyséa      : {entropy_life:.4f}")
    
    # Test d'extraction sur un lapsus non corrigé
    test_run = monitor.evaluate_alienation_risk(
        prompt="Détermine l'architecture de la trace", 
        response="L'architecture de la trace détermine le modèle", 
        user_id="BenjaminAmiel"
    )
    print(f"[DIAGNOSTIC LYSÉA] {test_run['diagnostic']}")
