from datetime import date, datetime, timezone
from enum import Enum
from unittest.mock import AsyncMock

import pytest
from app.models.events import Event
from app.repositories.events import EventRepository
from app.schemas.events import EventCreate
from sqlalchemy.ext.asyncio import AsyncSession


class RPGStatus(int, Enum):
    BOOKING = 1
    CANCELLATION = 2


class AsyncResult:
    def __init__(self, result):
        self._result = result


@pytest.fixture
def mock_db():
    return AsyncMock(spec=AsyncSession)


@pytest.fixture
def event_repository(mock_db):
    return EventRepository(db=mock_db)


@pytest.fixture
def sample_event_data():
    return {
        "id": 1,
        "hotel_id": 1,
        "timestamp": datetime.now(timezone.utc),
        "rpg_status": RPGStatus.BOOKING,
        "room_id": 101,
        "night_of_stay": date.today(),
    }


@pytest.mark.asyncio
async def test_create_event(event_repository, mock_db, sample_event_data):
    """
    Test the creation of an event using the EventRepository.
    """
    create_data = sample_event_data.copy()
    create_data.pop("id")
    event_create = EventCreate(**create_data)

    mock_db.commit = AsyncMock()
    mock_db.refresh = AsyncMock()

    created_event = await event_repository.create_event(event_create)

    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once_with(created_event)

    added_event = mock_db.add.call_args[0][0]
    assert added_event.hotel_id == create_data["hotel_id"]
    assert added_event.rpg_status == create_data["rpg_status"]
    assert added_event.room_id == create_data["room_id"]
    assert added_event.night_of_stay == create_data["night_of_stay"]
    assert added_event.timestamp == create_data["timestamp"]


@pytest.mark.asyncio
async def test_get_events_with_results(event_repository, mock_db):
    # Sample data for mock result
    sample_event = AsyncResult(
        [
            Event(
                id=1,
                hotel_id=1,
                timestamp=datetime.now(timezone.utc),
                rpg_status=RPGStatus.BOOKING,
                room_id=101,
                night_of_stay=date.today(),
            )
        ]
    )
    mock_db.execute = AsyncMock(return_value=sample_event)

    # Call get_events with filters
    events = await event_repository.get_events(hotel_id=1)

    assert mock_db.execute.called
    assert len(events) == 1
    assert events[0].hotel_id == 1
    assert events[0].rpg_status == RPGStatus.BOOKING
