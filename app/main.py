from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import calculations
from app.api.v1.endpoints import binomial_asset
from app.api.v1.endpoints import binomial_options
from app.api.v1.endpoints import asset_sim
from app.api.v1.endpoints import bs_op_val

app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to limit origins allowed to access your API
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods, or specify allowed methods like ["GET", "POST"]
    allow_headers=["*"],  # Allow all headers, or specify allowed headers
)

app.include_router(calculations.router, prefix="/calculations", tags=["calculations"])
app.include_router(binomial_asset.router, prefix="/binomial_asset", tags=["binomial_asset"])
app.include_router(binomial_options.router, prefix="/binomial_options", tags=["binomial_options"])
app.include_router(asset_sim.router, prefix="/asset_sim", tags=["asset_sim"])
app.include_router(bs_op_val.router, prefix="/bs_op_val", tags=["bs_op_val"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Calculation Service!"}

