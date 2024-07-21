import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.binomial_modelling.binomial_asset import BinomialModelling
import numpy as np


def test_binomial_asset_base():
    # Parameters
    S0 = 100  # Current stock price
    K = 100  # Strike price
    T = 1.0  # Time to maturity (1 year)
    r = 0.05  # Risk-free rate
    sigma = 0.2  # Volatility
    N = 4  # Number of time steps
    u, v  = 1.0604, 0.9431
    res = [[100, 0, 0, 0, 0],
           [94.31, 106.04, 0, 0, 0],
           [88.94376100000001, 100.006324, 112.444816, 0, 0],
           [83.88286099910002, 94.31596416440001, 106.04670596960001, 119.2364828864, 0],
           [79.10992620825122, 88.94938580344567, 100.01264839992977, 112.45192701016386, 126.43836645273856]]
    res = np.array(res)
    calculated_res = np.array(BinomialModelling.calculateAssetBase(S0, u, v, N))
    res_rounded = np.around(res, decimals=2)
    calculated_res_rounded = np.around(calculated_res, decimals=2)
    assert np.array_equal(res_rounded, calculated_res_rounded), f"Arrays are not equal:\nExpected:\n{res_rounded}\nGot:\n{calculated_res_rounded}"




def test_binomial_option_drift():
    S0 = 100  # Current stock price
    K = 100  # Strike price
    T = 1.0  # Time to maturity (1 year)
    r = 0.05  # Risk-free rate
    sigma = 0.2  # Volatility
    N = 3  # Number of time steps
    delta_t = T / N
