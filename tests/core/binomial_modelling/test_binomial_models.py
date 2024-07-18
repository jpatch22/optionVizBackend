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


    asset_prices = calculate_asset_prices(S0, u, d, N)

def test_binomial_option_drift():
    S0 = 100  # Current stock price
    K = 100  # Strike price
    T = 1.0  # Time to maturity (1 year)
    r = 0.05  # Risk-free rate
    sigma = 0.2  # Volatility
    N = 3  # Number of time steps
    delta_t = T / N
    u = np.exp(sigma * np.sqrt(delta_t))
    d = 1 / u
    p = (np.exp(r * delta_t) - d) / (u - d)

    asset_prices = calculate_asset_prices(S0, u, d, N)

    option_values_call = calculate_option_prices(asset_prices, K, r, delta_t, p, call_payoff)
    call_option_value = option_values_call[0, 0]
    print("Call Option Value:", call_option_value)

    option_values_put = calculate_option_prices(asset_prices, K, r, delta_t, p, put_payoff)
    put_option_value = option_values_put[0, 0]
    print("Put Option Value:", put_option_value)
    
