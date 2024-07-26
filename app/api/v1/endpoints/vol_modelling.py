from fastapi import APIRouter, HTTPException
from app.models.volatility import volRequest, volResponse

router = APIRouter()

@router.post("/", response_model=volResponse)
def calculate(request: volRequest):
    try:
        return volRequest
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

