from datetime import date, datetime, timezone
from enum import Enum

import pytest
from conftest import TEST_BASE_URL
from httpx import AsyncClient


class RPGStatus(Enum):
    BOOKING = 1
    CANCELLATION = 2


@pytest.mark.asyncio
async def test_create_event_success(client: AsyncClient):
    """
    Test successful event creation
    """
    event_data = {
        "hotel_id": 1,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "rpg_status": RPGStatus.BOOKING.value,
        "room_id": 101,
        "night_of_stay": str(date.today()),
    }

    response = await client.post(f"{TEST_BASE_URL}/events/", json=event_data)
    assert response.status_code == 200

    response_data = response.json()
    assert "id" in response_data
    assert response_data["hotel_id"] == event_data["hotel_id"]
    assert response_data["rpg_status"] == event_data["rpg_status"]
    assert response_data["room_id"] == event_data["room_id"]
    assert response_data["night_of_stay"] == event_data["night_of_stay"]


@pytest.mark.asyncio
async def test_create_event_missing_required_fields(client: AsyncClient):
    """
    Test event creation with missing required fields
    """
    incomplete_data = {
        "hotel_id": 1,
        "rpg_status": RPGStatus.BOOKING.value
        # timestamp, room_id, and night_of_stay
    }

    response = await client.post(f"{TEST_BASE_URL}/events/", json=incomplete_data)
    assert response.status_code == 422
