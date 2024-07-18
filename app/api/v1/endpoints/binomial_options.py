from app.models.binomial_option import BinomialOptionRequestBase, BinomialOptionRequestDrift
from app.models.binomial_option import BinomialOptionResponse
from fastapi import APIRouter, HTTPException
from typing import Union

router = APIRouter()

@router.post("/", response_model=BinomialOptionResponse)
def binomial_asset(request: Union[BinomialOptionRequestBase, BinomialOptionRequestDrift]):
    try:
        if isinstance(request, BinomialOptionRequestBase):
            return BinomialOptionResponse(
                    []
                    )
        elif isinstance(request, BinomialOptionRequestDrift):
            return BinomialOptionResponse(
                    []
                    )
        else:
            raise HTTPException(status_code=400, detail="Invalid request type")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

