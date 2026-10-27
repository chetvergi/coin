from fastapi.testclient import TestClient
import pytest

from app import app

client = TestClient(app)

def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_root():
    response = client.get('/')

    assert response.status_code == 200
    assert response.json()['message'] == "Подбросьте монетку"


def test_throw():
    client.get("/reset")
    client.get("/quantity?qu=3")
    
    response = client.get("/throw")
    assert response.status_code == 200

    results = response.json()
    assert isinstance(results, list)
    assert len(results) ==3
    for i in results:
        assert i in ["ОРЕЛ", "РЕШКА"]
    
def test_version():
    response = client.get("/version")

    assert response.status_code == 200
    assert "version" in response.json()
