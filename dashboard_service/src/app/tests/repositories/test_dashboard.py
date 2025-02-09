from datetime import datetime, timezone
from unittest.mock import patch

import pandas as pd
import pytest
from app.repositories.dashboard import DashboardRepository

TEST_BASE_URL = "http://test"


@pytest.mark.asyncio
async def test_dashboard_repository_invalid_csv():
    #  CSV file is invalid
    with patch("pandas.read_csv", side_effect=Exception("Invalid CSV")):
        repo = DashboardRepository(csv_path="test.csv")
        with pytest.raises(Exception, match="Error loading CSV file"):
            repo.get_dashboard_data(hotel_id=1, period="month")


@pytest.mark.asyncio
async def test_dashboard_repository_missing_columns():
    # CSV file is missing required columns
    mock_df = pd.DataFrame({"hotel_id": [1]})
    with patch("pandas.read_csv", return_value=mock_df):
        repo = DashboardRepository(csv_path="test.csv")
        # Expect an exception indicating missing columns
        with pytest.raises(Exception, match="Missing column in CSV"):
            repo.get_dashboard_data(hotel_id=1, period="month")


@pytest.mark.asyncio
async def test_dashboard_repository_success():
    #  Valid CSV file with correct data
    data = {
        "id": [1, 2],
        "hotel_id": [1, 1],
        "room_reservation_id": [
            "9f076c62-6666-49b2-8721-e118bd1d545c",
            "6221b2c8-129f-4759-a1f9-7897f0dbc2ca",
        ],
        "status": [1, 0],
        "event_timestamp": [
            datetime(2023, 1, 1, 12, 0, tzinfo=timezone.utc),
            datetime(2023, 2, 1, 12, 0, tzinfo=timezone.utc),
        ],
    }
    mock_df = pd.DataFrame(data)
    with patch("pandas.read_csv", return_value=mock_df):
        repo = DashboardRepository(csv_path="test.csv")
        # Get dashboard data for hotel_id=1 and period="month"
        result = repo.get_dashboard_data(hotel_id=1, period="month")
    # Assert that the result matches expected data
    assert result == {"2023-01": 1, "2023-02": 0}
