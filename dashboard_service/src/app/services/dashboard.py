import httpx
from app.repositories.dashboard import DashboardRepository
from app.schemas.dashboard import (
    DashboardErrorResponse,
    DashboardSuccessResponse,
    EventData,
)


class DashboardService:
    def __init__(
        self, repo: DashboardRepository, api_url="http://127.0.0.1:8000/api/events/"
    ):
        self.repo = repo
        self.api_url = api_url

    async def get_dashboard_data(self, hotel_id: int, period: str):
        """
        Get event and booking statistics from both the CSV and the Data Provider API.
        """
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{self.api_url}?hotel_id={hotel_id}")

                if response.status_code != 200:
                    return DashboardErrorResponse(
                        error=f"Failed to fetch event data. Status: {response.status_code}"
                    )

                event_data_raw = response.json()
        except httpx.HTTPError as e:
            return DashboardErrorResponse(error=f"HTTP error occurred: {str(e)}")
        except Exception as e:
            return DashboardErrorResponse(
                error=f"Unexpected error fetching event data: {str(e)}"
            )

        try:
            csv_data = self.repo.get_dashboard_data(hotel_id, period)
        except Exception as e:
            return DashboardErrorResponse(error=f"Error processing CSV data: {str(e)}")

        event_data = [EventData(**event) for event in event_data_raw]

        return DashboardSuccessResponse(
            hotel_id=hotel_id,
            period=period,
            csv_data=csv_data,
            event_data=event_data,
        )
