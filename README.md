# Backend for visualising option values

To allow calculations in Python

Run app:
uvicorn app.main:app --reload

Dependancies:
conda env create -f environment.yml
conda activate fastapi-env

Example Request:
curl -X POST "http://127.0.0.1:8000/calculations/" -H "Content-Type: application/json" -d '{"operation": "add", "a": 5, "b": 3}'

Swagger UI
http://127.0.0.1:8000/docs
