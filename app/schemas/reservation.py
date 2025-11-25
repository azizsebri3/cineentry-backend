from pydantic import BaseModel
from datetime import datetime

# ------------------------------------------------
# Pour la création (POST /reservation)
# ------------------------------------------------
class ReservationCreate(BaseModel):
    showtime_id: int
    seat_number: str


# ------------------------------------------------
# Pour la réponse API (GET / POST response)
# ------------------------------------------------
class ReservationResponse(BaseModel):
    id: int
    user_name: str
    showtime_id: int
    seat_number: str
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}
