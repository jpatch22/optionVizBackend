import pytest
from fastapi.testclient import TestClient
from app.main import app


def test_binomial_asset_base():
    # Parameters
    S0 = 100  # Current stock price
    K = 100  # Strike price
    T = 1.0  # Time to maturity (1 year)
    r = 0.05  # Risk-free rate
    sigma = 0.2  # Volatility
    N = 3  # Number of time steps



def test_binomial_option_drift():
    S0 = 100  # Current stock price
    K = 100  # Strike price
    T = 1.0  # Time to maturity (1 year)
    r = 0.05  # Risk-free rate
    sigma = 0.2  # Volatility
    N = 3  # Number of time steps
    delta_t = T / N
