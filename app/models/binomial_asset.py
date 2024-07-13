from pydantic import BaseModel
from typing import List, Optional

class BinomialAssetRequestBase(BaseModel):
    u: float
    v: float
    s: float
    numSteps: int

class BinomialAssetRequestDrift(BaseModel):
    vol: float
    numSteps: int
    s: float
    timeStep: float

class BinomialAssetResponse(BaseModel):
    asset_prices: List[List[float]]
    sdAssetChange: Optional[float] = None
    sdReturn: Optional[float] = None
    expReturn: Optional[float] = None

