from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from datetime import datetime
from typing import Dict

class EventBase(BaseModel):
    name: str
    description: Dict[str, str]  # Dictionary with language codes as keys
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
    id: Optional[str] = Field(alias='_id')

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
