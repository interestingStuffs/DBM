
from fastapi import APIRouter
from app.api.api_v1.endpoints import event, user

api_router = APIRouter()
api_router.include_router(event.router, prefix="/events", tags=["events"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
