from pydantic import BaseModel
from typing import List, Optional

class RowDataExtended(BaseModel):
    longShort: str = ''
    optionType: str = ''
    contractPrice: str = ''
    timeToExpiry: str = ''

class OptionPricingRequest(BaseModel):
    r: float  # Risk-free rate
    sigma: float  # Volatility
    s: float  # Stock price
    options: List[RowDataExtended]  # List of options

class OptionPricingResponse(BaseModel):
    optionPrices: List[List[float]]
    stock: List[float]
    time: List[float]
