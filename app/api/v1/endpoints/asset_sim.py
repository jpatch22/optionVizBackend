from app.models.asset_sim import AssetSimResponse, AssetSimRequest
from fastapi import APIRouter, HTTPException
from app.core.asset_sim.asset_sim import AssetSim

router = APIRouter()

@router.post("/", response_model=AssetSimResponse)
def asset_sim(request: AssetSimRequest):
    print(f"Running here: {request}")
    try:
        print("This thing")
        if isinstance(request, AssetSimRequest):
            print(f"here a;lsdkjf {request}")
            #res = AssetSim.doLognormalAssetWalk(
            #                request.s0,
            #                request.T,
            #                request.N,
            #                request.sigma,
            #                request.drift)
            res = AssetSim.doLognormalAssetWalk(1, 1, 1, 1, 5)
            print("hereasl;kfdj")
            print(res)
            return AssetSimResponse(assetPrices = res)
        else:
            raise HTTPException(status_code=400, detail="Invalid request type")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

