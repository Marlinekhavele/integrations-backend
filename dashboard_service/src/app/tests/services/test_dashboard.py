from unittest.mock import Mock, patch

import pytest
from app.schemas.dashboard import DashboardErrorResponse, DashboardSuccessResponse
from app.services.dashboard import DashboardService

TEST_BASE_URL = "http://test"


@pytest.mark.asyncio
async def test_get_dashboard_data_success():
    # Mock the repository to return predefined data
    mock_repo = Mock()
    mock_repo.get_dashboard_data.return_value = {"2023-01": 10, "2023-02": 15}

    service = DashboardService(repo=mock_repo)

    # Mock the API response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {
            "id": 1,
            "hotel_id": 1,
            "room_reservation_id": "6221b2c8-129f-4759-a1f9-7897f0dbc2ca",  # This is a random uuid
            "status": 1,
            "event_timestamp": "2023-01-01T12:00:00Z",
        },
        {
            "id": 2,
            "hotel_id": 1,
            "room_reservation_id": "9f076c62-6666-49b2-8721-e118bd1d545c",  # This is a random uuid
            "status": 0,
            "event_timestamp": "2023-02-01T12:00:00Z",
        },
    ]

    # Patch the AsyncClient to return our mock response
    with patch("httpx.AsyncClient") as MockAsyncClient:
        mock_client = MockAsyncClient.return_value
        mock_client.get.return_value = mock_response

        # Call the service method
        result = await service.get_dashboard_data(hotel_id=1, period="month")

    # Assert the result matches our expectations
    assert isinstance(result, DashboardSuccessResponse)
    assert result.hotel_id == 1
    assert result.period == "month"
    assert result.csv_data == {"2023-01": 10, "2023-02": 15}
    assert len(result.event_data) == 2


@pytest.mark.asyncio
async def test_get_dashboard_data_api_error():
    mock_repo = Mock()
    service = DashboardService(repo=mock_repo)

    # Trigger an API error
    with patch("httpx.AsyncClient") as MockAsyncClient:
        mock_client = MockAsyncClient.return_value
        mock_client.get.side_effect = Exception("API Error")

        # Call the service method
        result = await service.get_dashboard_data(hotel_id=1, period="month")

    # Assert that we get an error response
    assert isinstance(result, DashboardErrorResponse)
    assert "Unexpected error fetching event data" in result.error
