from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_analyze_positive():
    response = client.post(
        "/analyze",
        json=[{"text": "I love this product!"}]
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "label" in response.json()[0]
    assert "score" in response.json()[0]

def test_analyze_empty_text():
    response = client.post(
        "/analyze",
        json=[{"text": ""}]
    )
    assert response.status_code in (422, 500)
