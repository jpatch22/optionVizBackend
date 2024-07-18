from pydantic import BaseModel
from typing import List, Optional

class BinomialAssetRequestBase(BaseModel):
    s0: float # Current Prices
    u: float # increasing factor
    v: float
    N: int # number of steps
    K: float # strike price
    r: float # risk free interest rate
    T: float # time to expiry
    optionType: str

class BinomialAssetRequestVol(BaseModel):
    s0: float
    sigma: float # volatility
    T: float # time period
    N: int
    K: float # strike price
    r: float # risk free interest rate
    T: float # time to expiry
    optionType: str

class BinomialAssetResponse(BaseModel):
    asset_prices: List[List[float]]

