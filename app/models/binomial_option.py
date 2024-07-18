from pydantic import BaseModel
from typing import List, Optional

class BinomialOptionRequestBase(BaseModel):
    s0: float # Current Prices
    u: float # increasing factor
    v: float
    N: int # number of steps

class BinomialOptionRequestDrift(BaseModel):
    s0: float
    sigma: float # volatility
    T: float # time period
    N: int

class BinomialOptionResponse(BaseModel):
    optionPrices: List[List[float]]

