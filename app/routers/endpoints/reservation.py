from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.reservation import Reservation as ReservationModel
from app.models.showtime import Showtime as ShowtimeModel
from app.schemas.reservation import ReservationResponse, ReservationCreate
from app.services.reservation_service import (
    cancel_reservation_service,
    get_all_reservations,
    create_reservation_service,
    get_reservation_service,
    delete_reservation_service,
)


router = APIRouter()

# Get all reservations
@router.get("/", response_model=List[ReservationResponse])
def get_reservations(db: Session = Depends(get_db)):
    return get_all_reservations(db)


# Create a new reservation
@router.post("/", response_model=ReservationResponse)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    return create_reservation_service(reservation, db)

# Get a reservation by ID
@router.get("/{reservation_id}", response_model=ReservationResponse)
def get_reservation(reservation_id: int, db: Session = Depends(get_db)):
    return get_reservation_service(reservation_id, db)

# Delete a reservation by ID
@router.delete("/{reservation_id}", response_model=ReservationResponse)
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    return delete_reservation_service(reservation_id, db)


@router.patch("/{reservation_id}/cancel")
def cancel_reservation(reservation_id: int, db: Session = Depends(get_db)):
    """
    Annule une réservation (si le showtime est encore à venir).
    """
    return cancel_reservation_service(reservation_id, db)
