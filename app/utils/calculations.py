from app.models.calculation import CalculationRequest

def perform_calculation(request: CalculationRequest) -> float:
    if request.operation == "add":
        return request.a + request.b
    elif request.operation == "subtract":
        return request.a - request.b
    elif request.operation == "multiply":
        return request.a * request.b
    elif request.operation == "divide":
        if request.b == 0:
            raise ValueError("Division by zero is not allowed")
        return request.a / request.b
    else:
        raise ValueError("Invalid operation")

