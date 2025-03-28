# Génération de données synthétiques pour calories brûlées à vélo

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pour la reproductibilité
np.random.seed(42)

# Niveaux d'intensité et leurs METs associés
intensites = {
    'cool': 4.0,
    'endurance': 6.8,
    'rythme': 8.0,
    'rapide': 10.0,
    'competition': 12.0
}

# Générer les données
n = 500
poids = np.random.normal(75, 10, n).clip(50, 100)
duree_min = np.random.uniform(30, 180, n)
intensite = np.random.choice(list(intensites.keys()), n)
met = np.array([intensites[i] for i in intensite])
duree_h = duree_min / 60
calories = met * poids * duree_h
vitesse_moy = np.random.normal(25, 5, n).clip(15, 40)
distance_km = vitesse_moy * (duree_min / 60)

df = pd.DataFrame({
    'poids_kg': poids,
    'duree_min': duree_min,
    'vitesse_moyenne': vitesse_moy,
    'distance_km': distance_km,
    'intensite': intensite,
    'met': met,
    'calories_brulees': calories
})

df.to_csv("../data/dataset_synthetique_calories.csv", index=False)

# Affichage basique
print(df.head())

# Visualisation
sns.pairplot(df[['poids_kg', 'duree_min', 'vitesse_moyenne', 'distance_km', 'calories_brulees']])
plt.suptitle("Pairplot des variables", y=1.02)
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Corrélation entre variables")
plt.show()
