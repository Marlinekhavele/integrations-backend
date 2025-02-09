import pytest
from httpx import AsyncClient

TEST_BASE_URL = "http://test"


@pytest.mark.asyncio
async def test_get_dashboard_success(client: AsyncClient):
    """
    Test for successful retrieval of dashboard data
    """
    response = await client.get(f"{TEST_BASE_URL}/dashboard?hotel_id=1&period=month")

    assert response.status_code == 200

    response_data = response.json()

    assert "hotel_id" in response_data
    assert response_data["period"] == "month"
    assert isinstance(response_data["csv_data"], dict)
    assert "event_data" in response_data
    assert isinstance(response_data["event_data"], list)
