from fastapi import FastAPI, HTTPException
import pickle
import numpy as np

app2 = FastAPI()

with open(r'prediction_price_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app2.post("/predict-model/V1", description = 'Retourne un prix m2 moyen en Idf via un modèle entrainé en 2022' )
def prediction_Idf(longitude: float, latitude: float, n_pieces: int, code_postal: int):
    
    try:
        coordonnees = np.array([[latitude, longitude, n_pieces, code_postal]])
        result = model.predict(coordonnees)
        return {"prix_m2_moyen": result[0]}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur{str(e)}")
    

with open(r'decision_tree_model.pkl', 'rb') as model_file:
    model0 = pickle.load(model_file)

@app2.post("/predict-model/V0", description = 'Retourne un prix m2 moyen via un modèle entrainé à Paris pour un 4 pièces en 2022' )
def prediction_Paris4P(latitude: float, longitude: float):
    
    try:
        coordonnees = np.array([[latitude, longitude]])
        result = model0.predict(coordonnees)
        return {"prix_m2_moyen": result[0]}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur{str(e)}")