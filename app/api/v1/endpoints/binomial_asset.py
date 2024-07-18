from fastapi import APIRouter, HTTPException
from typing import Union
from app.core.binomial_modelling.binomial_asset import BinomialModelling
from app.models.binomial_asset import BinomialAssetRequestBase, BinomialAssetRequestVol, \
        BinomialAssetResponse


router = APIRouter()

@router.post("/", response_model=BinomialAssetResponse)
def binomial_asset(request: Union[BinomialAssetRequestVol, BinomialAssetRequestBase]):
    try:
        if isinstance(request, BinomialAssetRequestBase):
            return BinomialAssetResponse(
                    assetPrices = BinomialModelling.calculateAssetBase(
                        request.s0,
                        request.u,
                        request.v,
                        request.N
                        )
                    )
        elif isinstance(request, BinomialAssetRequestVol):
            return BinomialAssetResponse(
                    assetPrices = 
                    BinomialModelling.calculateBaseVol(
                        request.sigma,
                        request.s0,
                        request.T,
                        request.N
                        )
                    )
        else:
            raise HTTPException(status_code=400, detail="Invalid request type")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

