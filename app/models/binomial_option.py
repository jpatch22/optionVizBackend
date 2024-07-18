from pydantic import BaseModel
from typing import List, Optional

class BinomialOptionRequestBase(BaseModel):
    u: float
    v: float
    s: float
    numSteps: int
    p: float
    r: float

class BinomialOptionRequestDrift(BaseModel):
    vol: float
    numSteps: int
    s: float
    timeStep: float
    r: float

class BinomialOptionResponse(BaseModel):
    optionPrices: List[List[float]]

