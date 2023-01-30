import pickle 
import pandas as pd 
from fastapi import FastAPI 
from pydantic import BaseModel
# CREATION DE L'API 

# Ouvrir le modèle
with open('xgb.pkl','rb') as file:
    xgb = pickle.load(file)


app = FastAPI()

# Créer une classe qui hérite de BaseModel

class request_body(BaseModel):
    State : str
    NAICS : int
    Term : int
    FranchiseCode : int
    UrbanRural : int
    GrAppv : int


# Créer d'une route pour les requêtes

@app.post("/predict")

# fonction qui va à partir d'un df, donné une reponse 
def predict(data:request_body):
    new_data = pd.DataFrame(dict(data), index=[0]) 
    class_idx = xgb.predict(new_data)[0] 
    prediction = int(class_idx)
    if prediction  == 0:
        return "Le prêt est accepté"
    else: 
        return "Le prêt est refusé"

