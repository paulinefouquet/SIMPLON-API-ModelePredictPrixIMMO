# Simplon- API Modèle de prédiction de prix immobilier en Idf

##TODO
Implementer le lien latitude/longitude et code postal via des données externes, puis tester
Reentrainer le modele pour améliorer le score : score actuel du modele exposé:
Model is : RandomForestRegressor(max_depth=50, min_samples_leaf=20, n_estimators=500)
Score model on train is :2556.992814137017
Score model on test is :3451.922135492969

## Brief projet dans le cadre de developement d'app immo

Création d'une API REST pour exposer les données d'un modèle de prédiction de prix m2 moyen

## Python Version
Version python 3.11.5

## Datas :
le modèle entrainé sur un fichier transaction.csv (kaggle set)

## Structure :
api_prediction.py : le code principal de l'API

cleaning_et_preprocessing : pour transformer le fichier transactions.csv en transactions_idf.csv délimité à l'Idf en 2022  
ajout de variable prix m2 et type batiments

ProjetIMMO_model_IleDFrance.ipynb : ce code permet d'entrainer le modèle et de définir les hyperparamètres

## Prérequis

Besoin des packages et de leurs dépendences suivantes à installer avec le cpommande pip install

- uvicorn
    serveur web asynchrone  
    pour démarrer le serveur depuis le dossier MODELE_PREDICTION :
```
uvicorn mainapi_prediction:app2 --reload
```
- FastAPI
    librairie avec toutes les fonctions necessaires aux API
- numpy
- pandas
