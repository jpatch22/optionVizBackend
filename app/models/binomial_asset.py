from pydantic import BaseModel
from typing import List, Optional

class BinomialAssetRequestBase(BaseModel):
    s0: float # Current Prices
    u: float # increasing factor
    v: float
    N: int # number of steps

class BinomialAssetRequestVol(BaseModel):
    s0: float
    sigma: float # volatility
    T: float # time period
    N: int

class BinomialAssetResponse(BaseModel):
    assetPrices: List[List[float]]
