from fastapi import FastAPI

from pydantic import BaseModel
from joblib import dump, load
import logging

class User(BaseModel):
    token : str
    text : str


logging.basicConfig(filename='journal.log',encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

app=FastAPI()

#Création d'une premier point de terminaison de l'API appelé "welcome" souhaitant la bienvenue aux utilisateurs de l'API. 

@app.get("/welcome")
async def get():
    logging.info("Code 200 : l'utilisateur est parvenu sur la page welcome.") 
    return {"Message" : "Bonjour, ceci est la beta d'un algorithm d'analyse de sentiment",
                "Status Code": 200}


"""Création du second point de terminaison "sentiment" permettant d'effectuer la prédiction de sentiment à partir du texte fourni
en entrée. L'utilisateur fournit ici deux éléments : 
- un token, pour permettre d'accéder à l'API de manière sécurisée. Ce token devra
être fourni à chaque utilisateur de l'API pour que celle-ci puisse être utilisée. 
- Un texte à tester en entrée. 
Outre la prédiction, l'API intègre un système permettant de vérifier le token entrée, renvoyant une erreur si le token fourni n'est
pas le bon. """

@app.post("/sentiment")
async def post(text: User):
    token = text.token
    texte = text.text
    logging.info("L'utilisateur utilise l'algorithme")
    logging.info("Il soumet les données {} et {}".format(token,texte))
    #Vérification si tous les champs requis sont bien remplis. 
    set1 = {token, texte}

    res = set([token, texte])
    if set1 != res:
        missing_fields = ', '.join(set1.difference(res))
        logging.warn("{} manquant".format(missing_fields))
        return {"Message" : f"{missing_fields} missing",
                "Status Code": 400}
    


    #Vérification du token fourni
    if token != "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9":
        logging.error("Token invalide !")
        return {"Message" : "Token Invalide",
                "Status Code": 401}
    #clf_pipe = load('sentiment_pipe.joblib')
    #Ici on charge la nouvelle pipeline optimisée avec de nouveaux paramètres
    clf_pipe=load("pipeline_optimale.joblib")
    prediction = clf_pipe.predict([texte])[0]
    if prediction==1:
        prediction="Positif"
        logging.info("Le résultat obtenu est Positif.")
    else:
        prediction="Négatif"
        logging.info("Le résultat obtenu est Négatif.")

    logging.info("Application utilisée avec succès.")

    return {"text": texte,
    "prediction": prediction}
       
