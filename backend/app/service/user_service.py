from typing import List
from app.models.user import UserCreate, UserUpdate, UserInDB
from app.crud.user import create_user, get_user, update_user, delete_user, get_users

async def create_user_service(user: UserCreate) -> UserInDB:
    return await create_user(user)

async def get_user_service(user_id: str) -> UserInDB:
    return await get_user(user_id)

async def update_user_service(user_id: str, user: UserUpdate) -> UserInDB:
    return await update_user(user_id, user)

async def delete_user_service(user_id: str) -> bool:
    return await delete_user(user_id)

async def get_users_service(skip: int = 0, limit: int = 10) -> List[UserInDB]:
    return await get_users(skip, limit)
