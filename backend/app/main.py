from fastapi import FastAPI
from app.api.api_v1.endpoints import event

app = FastAPI()

app.include_router(event.router, prefix="/api/v1/events", tags=["events"])
