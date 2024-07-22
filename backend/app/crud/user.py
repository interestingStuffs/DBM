
from typing import List
from app.models.user import UserCreate, UserUpdate, UserInDB
from app.db.session import get_collection

async def create_user(user: UserCreate) -> UserInDB:
    collection = get_collection("users")
    result = await collection.insert_one(user.dict())
    return UserInDB(id=str(result.inserted_id), **user.dict())

async def get_user(user_id: str) -> UserInDB:
    collection = get_collection("users")
    user = await collection.find_one({"_id": user_id})
    if user:
        return UserInDB(**user)
    return None

async def update_user(user_id: str, user: UserUpdate) -> UserInDB:
    collection = get_collection("users")
    await collection.update_one({"_id": user_id}, {"$set": user.dict()})
    updated_user = await collection.find_one({"_id": user_id})
    return UserInDB(**updated_user)

async def delete_user(user_id: str) -> bool:
    collection = get_collection("users")
    result = await collection.delete_one({"_id": user_id})
    return result.deleted_count > 0

async def get_users(skip: int = 0, limit: int = 10) -> List[UserInDB]:
    collection = get_collection("users")
    users_cursor = collection.find().skip(skip).limit(limit)
    users = await users_cursor.to_list(length=limit)
    return [UserInDB(**user) for user in users]
