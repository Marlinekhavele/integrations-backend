from app.repositories.booking import DashboardRepository
from app.schemas.booking import DashboardResponse
from app.services.booking import DashboardService
from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/dashboard", response_model=DashboardResponse)
async def get_dashboard(
    hotel_id: int,
    period: str = Query(..., enum=["month", "day", "year"]),
):
    """
    Fetch dashboard analytics for a hotel.
    """
    repo = DashboardRepository()
    service = DashboardService(repo)
    return await service.get_dashboard_data(hotel_id, period)
