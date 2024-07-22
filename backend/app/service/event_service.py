from typing import List
from app.models.event import EventCreate, EventUpdate, EventInDB
from app.crud.event import create_event, get_event, update_event, delete_event, get_events

async def create_event_service(event: EventCreate) -> EventInDB:
    return await create_event(event)

async def get_event_service(event_id: str) -> EventInDB:
    return await get_event(event_id)

async def update_event_service(event_id: str, event: EventUpdate) -> EventInDB:
    return await update_event(event_id, event)

async def delete_event_service(event_id: str) -> bool:
    return await delete_event(event_id)

async def get_events_service(skip: int = 0, limit: int = 10) -> List[EventInDB]:
    return await get_events(skip, limit)
