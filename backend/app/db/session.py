from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection
from ..config import settings

def get_collection(collection_name: str) -> Collection:
    client = AsyncIOMotorClient(settings.MONGODB_URL)  # Use the URL from config
    db = client[settings.MONGODB_DB]  # Use the database name from config
    return db[collection_name]
