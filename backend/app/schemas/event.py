
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EventBase(BaseModel):
    name: str
    description: str
    location: str
    start_time: datetime
    end_time: datetime

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

class EventInDB(EventBase):
    id: str = Field(..., alias="_id")

