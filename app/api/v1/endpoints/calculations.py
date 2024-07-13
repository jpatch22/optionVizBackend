from fastapi import APIRouter, HTTPException
from app.models.calculation import CalculationRequest, CalculationResponse
from app.utils.calculations import perform_calculation

router = APIRouter()

@router.post("/", response_model=CalculationResponse)
def calculate(request: CalculationRequest):
    try:
        result = perform_calculation(request)
        return CalculationResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

