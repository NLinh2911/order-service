from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.base import Base
from app.db.base import engine
from app.api.v1 import (
    orders,
)
from app.core.config import settings

app = FastAPI()

# Allow requests from the different services
origins = [
    "http://localhost:8000",
    "http://localhost:8001",
    "http://localhost:8002",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def index():
    return {"message": "ORDER-SERVICE MICROSERVICE API"}


app.include_router(orders.router)
