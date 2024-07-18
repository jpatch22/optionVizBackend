from pydantic import BaseModel
from typing import List, Optional

class BinomialOptionRequestBase(BaseModel):
    s0: float # Current Prices
    u: float # increasing factor
    v: float
    N: int # number of steps
    K: float # strike price
    simga: float
    r: float # risk free interest rate
    T: float # time to expiry
    optionType: str

class BinomialOptionRequestVol(BaseModel):
    s0: float
    sigma: float # volatility
    T: float # time period
    N: int
    K: float # strike price
    r: float # risk free interest rate
    optionType: str

class BinomialOptionResponse(BaseModel):
    optionPrices: List[List[float]]

