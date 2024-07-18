import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestBinomialAsset:
    def test_binomial_option_base(self):
        request_data = {
            "s0": 100.0,
            "u": 1.1,
            "v": 0.9,
            "N": 3,
            "K": 100.0,
            "sigma": 0.2,
            "r": 0.05,
            "T": 1.0,
            "optionType": "europeanCall"
        }
        response = client.post("/binomial_options/", json=request_data)
        assert response.status_code == 200
        assert "optionPrices" in response.json()

    def test_binomial_option_vol(self):
        request_data = {
            "sigma": 0.2,
            "s0": 100.0,
            "T": 1.0,
            "N": 3,
            "K": 100.0,
            "r": 0.05,
            "optionType": "europeanPut"
        }
        response = client.post("/binomial_options/", json=request_data)
        assert response.status_code == 200
        assert "optionPrices" in response.json()

    def test_invalid_request_type(self):
        request_data = {
            "invalid_field": "invalid_value"
        }
        response = client.post("/binomial_options/", json=request_data)
        assert response.status_code == 422

    def test_invalid_option_type(self):
        request_data = {
            "s0": 100.0,
            "u": 1.1,
            "v": 0.9,
            "N": 3,
            "K": 100.0,
            "r": 0.05,
            "T": 1.0,
            "optionType": "unknown_option"
        }
        response = client.post("/binomial_options/", json=request_data)
        assert response.status_code == 422

