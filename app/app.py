import streamlit as st
import joblib
import numpy as np

# Chargement du modèle entraîné
model = joblib.load('model_calories.pkl')

# Configuration de la page
st.set_page_config(page_title="Calories à vélo", layout="centered")
st.title("🚴‍♂️ Prédicteur de calories brûlées à vélo")
st.markdown("Entrez les détails de votre sortie pour estimer les calories brûlées :")

# Champs de saisie utilisateur
poids = st.number_input("Poids (kg)", min_value=40.0, max_value=120.0, value=70.0)
duree = st.number_input("Durée de la sortie (minutes)", min_value=10, max_value=300, value=60)
distance = st.number_input("Distance (km)", min_value=1.0, max_value=200.0, value=25.0)
vitesse = distance / (duree / 60) if duree > 0 else 0.0  # km/h

# Intensité et MET
intensite_dict = {
    "Cool (20 km/h)" : 4.0,
    "Endurance (25 km/h)" : 6.8,
    "Rythmé (30 km/h)" : 8.0,
    "Rapide (35 km/h)" : 10.0,
    "Compétition (>35 km/h)" : 12.0
}
intensite_label = st.selectbox("Intensité de l'effort", list(intensite_dict.keys()))
met = intensite_dict[intensite_label]

# Bouton de prédiction
if st.button("🔍 Prédire les calories brûlées"):
    X_input = np.array([[poids, duree, distance, vitesse, met]])
    prediction = model.predict(X_input)[0]
    st.success(f"🔥 Estimation : **{prediction:.0f} kcal** brûlées pendant la sortie.")