from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection

def get_collection(collection_name: str) -> Collection:
    client = AsyncIOMotorClient("mongodb://localhost:27017")  # Ensure MongoDB URI is correct
    db = client["your_database_name"]
    return db[collection_name]
