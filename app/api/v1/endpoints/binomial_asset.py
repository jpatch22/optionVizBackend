from fastapi import APIRouter, HTTPException
from app.models.binomial_asset import BinomialAssetRequestBase, \
        BinomialAssetRequestDrift, BinomialAssetResponse
from typing import Union
from app.core.binomial_modelling.binomial_asset import binomial_asset_value_base, \
        binomial_asset_value_drift

router = APIRouter()

@router.post("/", response_model=BinomialAssetResponse)
def binomial_asset(request: Union[BinomialAssetRequestDrift, BinomialAssetRequestBase]):
    try:
        if isinstance(request, BinomialAssetRequestBase):
            valueTree = binomial_asset_value_base(
                    request.u,
                    request.v,
                    request.s,
                    request.numSteps
                )
            return BinomialAssetResponse(
                        asset_prices = valueTree
                   )
        elif isinstance(request, BinomialAssetRequestDrift):
            valueTree = binomial_asset_value_drift(
                        request.s,
                        request.vol,
                        request.timeStep,
                        request.numSteps
                    )
            return BinomialAssetResponse(
                        asset_prices = valueTree
                   )
        else:
            raise HTTPException(status_code=400, detail="Invalid request type")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

