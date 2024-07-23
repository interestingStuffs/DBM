from fastapi import APIRouter, HTTPException
from app.models.event import EventCreate, EventUpdate, EventInDB
from app.service.event_service import create_event_service, get_event_service, update_event_service, delete_event_service, get_events_service
from typing import List
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=EventInDB)
async def create_event_route(event: EventCreate):
    return await create_event_service(event)

@router.get("/{event_id}", response_model=EventInDB)
async def get_event_route(event_id: str):
    event = await get_event_service(event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.put("/{event_id}", response_model=EventInDB)
async def update_event_route(event_id: str, event: EventUpdate):
    updated_event = await update_event_service(event_id, event)
    if updated_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated_event

@router.delete("/{event_id}", response_model=dict)
async def delete_event_route(event_id: str):
    success = await delete_event_service(event_id)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": "Event deleted successfully"}

@router.get("/", response_model=List[EventInDB])
async def list_events(skip: int = 0, limit: int = 10):
    return await get_events_service(skip=skip, limit=limit)

@router.get("/range", response_model=List[EventInDB])
async def get_events_by_date_range(start_date: datetime, end_date: datetime, skip: int = 0, limit: int = 10):
    return await get_events_by_date_range_service(start_date, end_date, skip, limit)
