
from fastapi import FastAPI

from routers import users

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to my FastAPI application!"
    }


app.include_router(
    users.router,
    prefix="/users",
    tags=["Users"]
)
