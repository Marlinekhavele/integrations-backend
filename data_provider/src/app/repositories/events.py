# data_provider/repository/event_repository.py
import uuid
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.deps import get_db_session
from app.models.events import Event
from datetime import date
from typing import List, Optional


class EventRepository:
    def __init__(self, db: AsyncSession = Depends(get_db_session)):
        self.db = db

    async def create_event(self, event_data):
        """
        Creates a new event in the database.
        """
        new_event = Event(**event_data.dict())
        self.db.add(new_event)
        await self.db.commit()
        await self.db.refresh(new_event)
        return new_event

    async def get_events(
        self,
        hotel_id: int,
        from_date: Optional[date] = None,
        to_date: Optional[date] = None,
        rpg_status: Optional[int] = None,
        room_id: Optional[int] = None,
        night_of_stay_gte: Optional[date] = None,
        night_of_stay_lte: Optional[date] = None,
    ) -> List[Event]:
        """
        Fetches events based on filters, sorted by timestamp in ascending order.
        """

        query = select(Event).where(Event.hotel_id == hotel_id)

        if from_date:
            query = query.where(Event.timestamp >= from_date)
        if to_date:
            query = query.where(Event.timestamp <= to_date)
        if rpg_status:
            query = query.where(Event.rpg_status == rpg_status)
        if room_id:
            query = query.where(Event.room_id == room_id)
        if night_of_stay_gte:
            query = query.where(Event.night_of_stay >= night_of_stay_gte)
        if night_of_stay_lte:
            query = query.where(Event.night_of_stay <= night_of_stay_lte)

        query = query.order_by(Event.timestamp.asc())

        results = await self.db.execute(query)
        return results.scalars().all()
