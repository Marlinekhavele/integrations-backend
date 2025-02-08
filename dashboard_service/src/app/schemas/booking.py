from typing import Dict

from pydantic import BaseModel


class DashboardResponse(BaseModel):
    """
    Schema for returning aggregated dashboard data.
    """

    hotel_id: int
    period: str
    data: Dict[str, int]

    class Config:
        orm_mode = True
