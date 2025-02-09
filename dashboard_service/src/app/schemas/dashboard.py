from typing import Dict, List, Union

from pydantic import BaseModel


class EventData(BaseModel):
    hotel_id: int
    id: int
    rpg_status: int
    night_of_stay: str
    room_id: int


class DashboardSuccessResponse(BaseModel):
    hotel_id: int
    period: str
    csv_data: Dict[str, int]
    event_data: Union[List[EventData], Dict]

    class Config:
        orm_mode = True


class DashboardErrorResponse(BaseModel):
    """
    Schema for error response.
    """

    error: str


DashboardResponse = Union[DashboardSuccessResponse, DashboardErrorResponse]
