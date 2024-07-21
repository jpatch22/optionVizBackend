from pydantic import BaseModel
from typing import List

class AssetSimRequest(BaseModel):
    s0: float # Current Prices
    N: int # number of steps
    sigma: float
    T: float # time to expiry
    drift: float

class AssetSimResponse(BaseModel):
    assetPrices: List[List[float]]

