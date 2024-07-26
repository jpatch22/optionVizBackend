from fastapi import APIRouter, HTTPException
from app.models.greeks import GreekRequest, GreekResponse

router = APIRouter()

@router.post("/", response_model=GreekResponse)
def calculate(request: GreekRequest):
    try:
        return GreekResponse()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

