from pydantic import BaseModel
from datetime import datetime

class ReservationBase(BaseModel):
    user_name: str
    showtime_id: int
    seat_number: str


class ReservationCreate(ReservationBase):
    pass


class ReservationResponse(ReservationBase):
    id: int
    status: str
    created_at: datetime
    model_config = {"from_attributes": True}
