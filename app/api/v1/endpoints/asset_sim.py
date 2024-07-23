from app.models.asset_sim import AssetSimResponse, AssetSimRequest
from fastapi import APIRouter, HTTPException
from app.core.asset_sim.asset_sim import AssetSim

router = APIRouter()

@router.post("/", response_model=AssetSimResponse)
def asset_sim(request: AssetSimRequest):
    try:
        if isinstance(request, AssetSimRequest):
            res = AssetSim.doLognormalAssetWalk(request.s0, request.T, request.N, request.sigma, request.drift)
            print(res)
            return AssetSimResponse(assetPrices = res)
        else:
            raise HTTPException(status_code=400, detail="Invalid request type")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

