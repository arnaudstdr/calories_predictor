import streamlit as st
import joblib
import pandas as pd
import os

# Chargement du modèle entraîné
model_path = os.path.join(os.path.dirname(__file__), "model_calories.pkl")
model = joblib.load(model_path)

# Configuration de la page
st.set_page_config(page_title="Calories à vélo", layout="centered")
st.title("🚴‍♂️ Prédicteur de calories brûlées à vélo (avec fréquence cardiaque)")
st.markdown("Entrez les détails de votre sortie pour estimer les calories brûlées :")

# Champs de saisie utilisateur
poids = st.number_input("Poids (kg)", min_value=40.0, max_value=120.0, value=70.0)
duree = st.number_input("Durée de la sortie (minutes)", min_value=10, max_value=300, value=60)
distance = st.number_input("Distance (km)", min_value=1.0, max_value=200.0, value=25.0)
vitesse = distance / (duree / 60) if duree > 0 else 0.0  # km/h
fc_moy = st.number_input("Fréquence cardiaque moyenne (bpm)", min_value=80, max_value=220, value=140)


# Bouton de prédiction
if st.button("🔍 Prédire les calories brûlées"):
    X_input = pd.DataFrame([{
        'poids_kg': poids,
        'duree_min': duree,
        'vitesse_moyenne': vitesse,
        'distance_km': distance,
        'fc_moyenne': fc_moy
    }])
    prediction = model.predict(X_input)[0]
    st.success(f"🔥 Estimation : **{prediction:.0f} kcal** brûlées pendant la sortie.")