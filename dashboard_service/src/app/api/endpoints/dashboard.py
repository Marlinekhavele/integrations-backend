from app.repositories.dashboard import DashboardRepository
from app.schemas.dashboard import DashboardResponse
from app.services.dashboard import DashboardService
from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/dashboard", response_model=DashboardResponse)
async def get_dashboard(
    hotel_id: int,
    period: str = Query(..., enum=["month", "day", "year"]),
):
    """
    Fetch dashboard analytics for bookings in a hotel.
    """
    repo = DashboardRepository()
    service = DashboardService(repo)
    return await service.get_dashboard_data(hotel_id, period)
