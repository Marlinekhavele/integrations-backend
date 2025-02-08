from app.database.base import Base
from sqlalchemy import Column, DateTime, Integer, String


class BookingStats(Base):
    __tablename__ = "booking_stats"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, nullable=False)
    room_reservation_id = Column(String, nullable=False, unique=True)
    status = Column(Integer, nullable=False)
    event_timestamp = Column(DateTime, nullable=False)
