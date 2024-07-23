from typing import List
from app.models.event import EventCreate, EventUpdate, EventInDB
from app.db.session import get_collection
from bson import ObjectId
from datetime import datetime

async def create_event(event: EventCreate) -> EventInDB:
    collection = get_collection("events")
    result = await collection.insert_one(event.dict(by_alias=True))
    return EventInDB(id=str(result.inserted_id), **event.dict())  # Convert ObjectId to str

async def get_event(event_id: str) -> EventInDB:
    collection = get_collection("events")
    event = await collection.find_one({"_id": ObjectId(event_id)})
    if event:
        return EventInDB(**{**event, '_id': str(event['_id'])})  # Convert ObjectId to str
    return None

async def update_event(event_id: str, event: EventUpdate) -> EventInDB:
    collection = get_collection("events")
    await collection.update_one({"_id": ObjectId(event_id)}, {"$set": event.dict(exclude_unset=True, by_alias=True)})
    updated_event = await collection.find_one({"_id": ObjectId(event_id)})
    return EventInDB(**{**updated_event, '_id': str(updated_event['_id'])})  # Convert ObjectId to str

async def delete_event(event_id: str) -> bool:
    collection = get_collection("events")
    result = await collection.delete_one({"_id": ObjectId(event_id)})
    return result.deleted_count > 0

async def get_events(skip: int = 0, limit: int = 10) -> List[EventInDB]:
    collection = get_collection("events")
    events_cursor = collection.find().skip(skip).limit(limit)
    events = await events_cursor.to_list(length=limit)
    return [EventInDB(**{**event, '_id': str(event['_id'])}) for event in events]  # Convert ObjectId to str

async def get_events_by_date_range(start_date: datetime, end_date: datetime, skip: int = 0, limit: int = 10) -> List[EventInDB]:
    collection = get_collection("events")
    query = {"start_time": {"$gte": start_date}, "end_time": {"$lte": end_date}}
    events_cursor = collection.find(query).skip(skip).limit(limit)
    events = await events_cursor.to_list(length=limit)
    return [EventInDB(**{**event, '_id': str(event['_id'])}) for event in events]
