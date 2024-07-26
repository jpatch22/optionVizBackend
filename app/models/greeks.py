from pydantic import BaseModel

class GreekRequest(BaseModel):
    optionPrices: str
    time: float
    stockPrices: float

class GreekResponse(BaseModel):
    delta: float
    gamma: float
    speed: float
    vega: float
    rho: float

