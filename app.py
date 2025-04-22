import streamlit as st
from Big_Bang_Final import BigBangAI

# Titre principal
st.title("BigBangAI — Intelligence Évolutive en Action")

# Sous-titre
st.markdown("**Fusion du savoir public et privé pour générer des hypothèses inédites.**")

# Initialisation du modèle
model = BigBangAI()

# Zone de saisie utilisateur
user_input = st.text_input("Entrez une intuition, une question, ou une observation du réel :")

# Traitement et affichage
if user_input:
    hypothesis = model.detect_emerging_patterns(user_input)
    st.markdown("### Réponse de BigBangAI :")
    st.success(hypothesis)