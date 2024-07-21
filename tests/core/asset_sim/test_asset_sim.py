import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.asset_sim.asset_sim import AssetSim
import numpy as np

def test_asset_sim():
    # Parameters
    N = 10
    T = 1
    sigma = .12
    s = 100
    drift = .12
    
    exp = np.linspace(0, T, num=N)
    print(AssetSim.doLognormalAssetWalk(s, T, N, sigma, drift))
    #assert np.array_equal(exp, AssetSim.doLognormalAssetWalk(s, T, N, sigma, drift)), f"Arrays are not equal"

