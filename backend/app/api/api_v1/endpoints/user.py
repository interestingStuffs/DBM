from fastapi import APIRouter, HTTPException
from app.models.user import UserCreate, UserUpdate, UserInDB
from app.service.user_service import create_user_service, get_user_service, update_user_service, delete_user_service, get_users_service
from typing import List

router = APIRouter()

@router.post("/", response_model=UserInDB)
async def create_user_route(user: UserCreate):
    return await create_user_service(user)

@router.get("/{user_id}", response_model=UserInDB)
async def get_user_route(user_id: str):
    user = await get_user_service(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserInDB)
async def update_user_route(user_id: str, user: UserUpdate):
    updated_user = await update_user_service(user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}", response_model=dict)
async def delete_user_route(user_id: str):
    success = await delete_user_service(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

@router.get("/", response_model=List[UserInDB])
async def list_users(skip: int = 0, limit: int = 10):
    return await get_users_service(skip=skip, limit=limit)
