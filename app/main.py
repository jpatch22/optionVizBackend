from fastapi import FastAPI
from app.api.v1.endpoints import calculations
from app.api.v1.endpoints import binomial_asset

app = FastAPI()

app.include_router(calculations.router, prefix="/calculations", tags=["calculations"])
app.include_router(binomial_asset.router, prefix="/binomial_asset", tags=["binomial_asset"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Calculation Service!"}

