from app.models.binomial_option import BinomialOptionRequestBase, BinomialOptionRequestVol
from app.models.binomial_option import BinomialOptionResponse
from app.core.binomial_modelling.binomial_asset import BinomialModelling
from app.utils.payoffs import OptionPayoffFunctions
from fastapi import APIRouter, HTTPException
from typing import Union

router = APIRouter()

@router.post("/", response_model=BinomialOptionResponse)
def binomial_asset(request: Union[BinomialOptionRequestBase, BinomialOptionRequestVol]):
    print("JACK RUNNING HERE")
    try:
        if isinstance(request, BinomialOptionRequestBase):
            return BinomialOptionResponse(
                    optionPrices = BinomialModelling.calculateOptionBase(
                        request.s0,
                        request.u,
                        request.v,
                        request.sigma,
                        request.N,
                        request.K,
                        request.r,
                        request.T,
                        OptionPayoffFunctions.payoff_map[request.optionType]
                        )
                    )
        elif isinstance(request, BinomialOptionRequestVol):
            return BinomialOptionResponse(
                    optionPrices = BinomialModelling.calculateOptionVol(
                        request.sigma,
                        request.s0,
                        request.T,
                        request.N,
                        request.K,
                        request.r,
                        OptionPayoffFunctions.payoff_map[request.optionType]
                        )
                    )
        else:
            raise HTTPException(status_code=400, detail="Invalid request type")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

