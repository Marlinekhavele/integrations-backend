from sqlalchemy import Column, Integer, Date, Enum
from sqlalchemy.dialects.postgresql import TIMESTAMP
from app.database.base import Base
from app.schemas.enums.status import RPGStatus  

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, nullable=False)
    timestamp = Column(TIMESTAMP(timezone=True), nullable=False)
    rpg_status = Column(Enum(RPGStatus), nullable=False)
    room_id = Column(Integer, nullable=False)
    night_of_stay = Column(Date, nullable=False)
    # room_reservation_id = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
