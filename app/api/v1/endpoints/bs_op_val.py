from app.core.black_scholes.option_valuing import BSOptionValues
from app.models.bs_op_val import OptionPricingRequest, OptionPricingResponse
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/", response_model=OptionPricingResponse)
def optionPricing(request: OptionPricingRequest):
    try:
        if isinstance(request, OptionPricingRequest):
            print(f"Got request : {request}")
            vals, time, stock = BSOptionValues.getOptionVal(
                        request.options,
                        request.r,
                        request.sigma,
                        request.s
                        )
            return OptionPricingResponse(optionPrices = vals, time = time, stock = stock)
        else:
            raise HTTPException(status_code=400, detail="Invalid request type")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

