from typing import Dict, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class EventBase(BaseModel):
    name: str
    description: Dict[str, str]
    location: str
    start_time: datetime
    end_time: datetime

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[Dict[str, str]] = None
    location: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

class EventInDB(EventBase):
    id: Optional[str] = Field(default=None, alias='_id')
