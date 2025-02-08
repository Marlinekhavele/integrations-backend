from pydantic import BaseModel
from datetime import datetime, date
# import uuid
from app.schemas.enums.status import RPGStatus  

class EventCreate(BaseModel):
    """
    Schema for creating a new event
    """
    hotel_id: int
    timestamp: datetime
    rpg_status: RPGStatus
    room_id: int
    night_of_stay: date
    # room_reservation_id: uuid.UUID

class EventResponse(EventCreate):
    """
    Schema for returning event data
    """
    id: int

    class Config:
        orm_mode = True
