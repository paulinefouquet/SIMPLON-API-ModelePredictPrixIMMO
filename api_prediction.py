from fastapi import FastAPI, HTTPException
import pickle
import numpy as np

app2 = FastAPI()

with open(r'C:\Users\Utilisateur\Desktop\Dev IA\Semaine 03bis\Simplon-MODELE_PREDICTION\prediction_price_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app2.post("/predict-model", description = 'Retourne un prix m2 moyen en Idf via un modèle entrainé en 2022' )
def prediction(longitude: float, latitude: float, n_pieces: int, code_postal: int):
    
    try:
        #transformation des paramètres en un objet valide pour le modele
        coordonnees = np.array([[latitude, longitude, n_pieces, code_postal]])
        result = model.predict(coordonnees)
        return {"prix_m2_moyen": result[0]}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur{str(e)}")