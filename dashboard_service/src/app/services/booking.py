import httpx
from app.repositories.booking import DashboardRepository


class DashboardService:
    def __init__(
        self, repo: DashboardRepository, api_url="http://data-provider:8000/api/events/"
    ):
        self.repo = repo
        self.api_url = api_url

    async def get_dashboard_data(self, hotel_id: int, period: str):
        """
        Get event statistics from both the CSV and the Data Provider API.
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.api_url}?hotel_id={hotel_id}")

            # Handle API failure
            if response.status_code != 200:
                return {"error": "Failed to fetch event data from Data Provider"}

            event_data = response.json()

        # Combine API event data with CSV-based analytics
        csv_data = self.repo.get_dashboard_data(hotel_id, period)

        return {
            "hotel_id": hotel_id,
            "period": period,
            "csv_data": csv_data,
            "event_data": event_data,
        }
