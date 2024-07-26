from pydantic import BaseModel
from typing import List

class volRequest(BaseModel):
    ticker: str
    volatilityModel: str
    fitType: str

class volResponse(BaseModel):
    prices: List[float]
    volatility: List[float]

