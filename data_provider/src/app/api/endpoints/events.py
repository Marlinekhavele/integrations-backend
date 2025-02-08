import uuid
from datetime import date
from typing import List, Optional

from app.repositories.events import EventRepository
from app.schemas.events import EventCreate
from fastapi import APIRouter, Depends, Query

router = APIRouter()


@router.post("/events/")
async def create_event(
    event: EventCreate, repo: EventRepository = Depends(EventRepository)
):
    """
    Create an Event and store it in the database.
    """
    new_event = await repo.create_event(event)
    return new_event


@router.get("/events/")
async def get_events(
    hotel_id: int,
    from_date: Optional[date] = Query(None, description="Start date of the event"),
    to_date: Optional[date] = Query(None, description="End date of the event"),
    rpg_status: Optional[int] = Query(
        None, description="1 - booking, 2 - cancellation"
    ),
    room_id: Optional[int] = Query(None, description="Room ID"),
    night_of_stay_gte: Optional[date] = Query(None, description="Start date of stay"),
    night_of_stay_lte: Optional[date] = Query(None, description="End date of stay"),
    repo: EventRepository = Depends(EventRepository),
):
    """
    Get all events for a particular hotel with optional filters.
    - `hotel_id` (required) → The hotel to filter events for
    - `from_date` → Filter events from this timestamp
    - `to_date` → Filter events until this timestamp
    - `rpg_status` → Booking (1) or Cancellation (2)
    - `room_id` → Filter events for a specific room
    - `night_of_stay_gte` → Minimum stay date
    - `night_of_stay_lte` → Maximum stay date
    """
    return await repo.get_events(
        hotel_id,
        from_date,
        to_date,
        rpg_status,
        room_id,
        night_of_stay_gte,
        night_of_stay_lte,
    )
