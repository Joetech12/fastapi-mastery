
import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from routers import users, products


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug
)


# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Custom middleware
@app.middleware("http")
async def add_process_time_header(
    request: Request,
    call_next
):

    start_time = time.perf_counter()

    response = await call_next(request)

    process_time = time.perf_counter() - start_time

    response.headers["X-Process-Time"] = str(process_time)

    return response


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
