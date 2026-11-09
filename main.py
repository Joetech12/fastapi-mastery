
from fastapi import FastAPI

from utils.calculator import add, multiply

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}


@app.get("/calculate")
def calculate():
    addition = add(10, 5)
    multiplication = multiply(10, 5)

    return {
        "addition": addition,
        "multiplication": multiplication
    }
