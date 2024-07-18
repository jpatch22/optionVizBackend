import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI Calculation Service!"}

def test_calculate_binomial_asset_request_base():
    response = client.post(
        "/binomial_asset/",
        json={
            "u": 1.1,
            "v": 0.9,
            "s0": 100,
            "N": 10
        }
    )
    assert response.status_code == 200
    assert "assetPrices" in response.json()

def test_calculate_binomial_asset_request_drift():
    response = client.post(
        "/binomial_asset/",
        json={
            "s0": 100,
            "sigma": 0.2,
            "T": 1,
            "N": 10
        }
    )
    assert response.status_code == 200
    assert "assetPrices" in response.json()

