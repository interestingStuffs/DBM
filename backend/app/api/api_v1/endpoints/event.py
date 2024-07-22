from fastapi import APIRouter, HTTPException
from app.models.event import EventCreate, EventUpdate, EventInDB
from app.crud.event import create_event, get_event, update_event, delete_event, get_events
from typing import List

router = APIRouter()

@router.post("/", response_model=EventInDB)
async def create_event_route(event: EventCreate):
    return await create_event(event)

@router.get("/{event_id}", response_model=EventInDB)
async def get_event_route(event_id: str):
    event = await get_event(event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.put("/{event_id}", response_model=EventInDB)
async def update_event_route(event_id: str, event: EventUpdate):
    updated_event = await update_event(event_id, event)
    if updated_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated_event

@router.delete("/{event_id}", response_model=dict)
async def delete_event_route(event_id: str):
    success = await delete_event(event_id)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": "Event deleted successfully"}

@router.get("/", response_model=List[EventInDB])
async def list_events(skip: int = 0, limit: int = 10):
    return await get_events(skip=skip, limit=limit)
