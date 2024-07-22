from fastapi import FastAPI
from app.api.api_v1.endpoints import event, user

app = FastAPI()

app.include_router(event.router, prefix="/api/v1/events", tags=["events"])
app.include_router(user.router, prefix="/api/v1/users", tags=["users"])
