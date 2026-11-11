
from fastapi import FastAPI

from core.config import settings
from routers import users, products


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug
)


@app.get("/")
def home():
    return {
        "message": f"Welcome to {settings.app_name}!",
        "environment": settings.environment
    }


app.include_router(
    users.router,
    prefix="/users",
    tags=["Users"]
)

app.include_router(
    products.router,
    prefix="/products",
    tags=["Products"]
)
