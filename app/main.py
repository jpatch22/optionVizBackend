from fastapi import FastAPI
from app.api.v1.endpoints import calculations

app = FastAPI()

app.include_router(calculations.router, prefix="/calculations", tags=["calculations"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Calculation Service!"}

