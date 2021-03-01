from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get():
    response = client.get("/welcome")
    assert response.status_code==200
    assert response.json() == {"Message" : "Bonjour, ceci est la beta d'un algorithm d'analyse de sentiment",
                "Status Code": 200}

def test_invalide_token():
    response=client.post("/sentiment",
    json={"token" : "metal",
    "text": "super"})
    assert response.status_code == 200
    assert response.json() == {"Message" : "Token Invalide",
                "Status Code": 401}
    
def test_prediction():
    response=client.post("/sentiment",
    json={"token" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
    "text": "super"})
    assert response.status_code == 200
    assert response.json() == {"text": "super",
    "prediction": "Positif"}
    