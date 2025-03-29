# 🚴‍♂️ Calories Predictor - Cyclisme & Machine Learning
Ce projet est une application de prédiction de **calories brûlées lors d'une sortie à vélo**, vasée sur un **modèle de machine learning entraîné sur un dataset synthétique réaliste**.
> Il s'agit d'un projet personnel mêlant passion pour le cyclisme, intérêt pour la physiologie et compétences en data science.

---

## 📦 Fonctionnalités
- Prédiction des calories brûlées à partie de :
  - Poids du cycliste
  - Durée de la sortie
  - Distance parcourue
  - Vitesse moyenne (calculé automatiquement)
  - Fréquence cardiaque moyenne 🫀
- Interface web interactive avec **Streamlit**
- Modèle de régression basé sur **Random Forest (sklearn)**

---

## 📊 Dataset synthétique
Une dataset de 500 lignes a été **généré artificiellement** avec :
- des âges simulés (16 à 65 ans)
- une FC mac calculée via 220 - âge
- une FC moyenne simulée selon l'intensité (% de FC max)
- un calcul des calories via une formule physiologique :
```python
 calories_par_min = (-55.0969 + 0.6309 * np.array(fc_moyenne) + 0.1988 * poids + 0.2017 * ages) / 4.184
calories = calories_par_min * duree_min
```
📁 Chemin : `data/dataset_synthetique_calories.csv`

---

## 🧠 Modélisation

- **Modèles testés** : Linear Regression & Random Forest Regressor
- **Performance (test set)** :
  - Régression linéaire : MAE = 153.56 kcal / RMSE = 191.98 kcal
  - Random Forest : MAE = 75.94 kcal / RMSE = 100.18 kcal

> Le modèle Random Forest permet de diviser par deux l'erreur moyenne par rapport à la régression linéaire, ce qui confirme sa capacité à capturer les relations non linéaires complexes entre les variables physiologiques et la dépense énergétique.

> L’augmentation des erreurs par rapport à la première version du projet (avec une formule simplifiée) est normale : le nouveau calcul des calories est basé sur une formule physiologique réaliste intégrant plusieurs facteurs (FC, poids, âge). Le modèle est donc confronté à une variabilité plus proche du monde réel.

---

## 🚀 Application Streamlit
Accessible localement via :
```bash
cd app
streamlit run app.py
```
📄 L'utilisateur entre ses données et l'app prédit les calories brûlées avec une estimation réaliste (en kcal).
📁 Fichier : `app/app.py`

---

## 🔧 Installation locale
```bash
git clone https://github.com/ton-profil/calories_predictor.git
cd calories_predictor
conda create -n calories_ml python=3.10
conda activate calories_ml
pip install -r requirements.txt
```

---

## 📈 Amélioration futures
- Intégration de données réelles (montre connectée, capteurs)
- Analyse du **niveau de fatigue/récupération** (projet 2 en cours)
- Ajout de visualisation dynamique dans Streamlit
- Déploiement en ligne via Streamlit Cloud

---

## 👨‍💻 Auteur
**Arnaud STADLER** - Développeur & passioné de cyclisme / data / IA
> Ce projet s'inscrit dans mon parcours de reconversion vers le Machine Learning. Il est 100% open-source et pédagogique.
💬 N'hésiter pas à ouvrir une issue ou à me contacter pour échanger 🚀