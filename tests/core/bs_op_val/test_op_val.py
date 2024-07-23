import pytest
from app.core.black_scholes.option_valuing import BSOptionValues

def test_call_value():
    S = 100  # Current stock price
    E = 100  # Strike price
    vol = 0.2  # Volatility
    r = 0.05  # Risk-free interest rate
    T = 1  # Time to maturity (in years)
    t = 0  # Current time

    expected_call_value = 10.45  # Approximate expected value
    call_value = BSOptionValues.getCallValue(t, S, E, vol, r, T)
    assert pytest.approx(call_value, 0.01) == expected_call_value

def test_put_value():
    S = 100  # Current stock price
    E = 100  # Strike price
    vol = 0.2  # Volatility
    r = 0.05  # Risk-free interest rate
    T = 1  # Time to maturity (in years)
    t = 0  # Current time

    expected_put_value = 5.57  # Approximate expected value
    put_value = BSOptionValues.getPutValue(t, S, E, vol, r, T)
    assert pytest.approx(put_value, 0.01) == expected_put_value
