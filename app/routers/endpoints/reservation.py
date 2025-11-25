from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.core.deps import get_current_user
from app.core.security import require_role
from app.schemas.reservation import ReservationResponse, ReservationCreate
from app.services.reservation_service import (
    cancel_reservation_service,
    get_all_reservations,
    create_reservation_service,
    get_reservation_service,
    delete_reservation_service,
)

router = APIRouter()

# Admin-only: see all reservations
@router.get("/", response_model=List[ReservationResponse])
def get_reservations(
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin")) # que l admin peut voir toutes les réservations 
):
    return get_all_reservations(db)

# User: create reservation
@router.post("/", response_model=ReservationResponse)
def create_reservation(
    reservation: ReservationCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return create_reservation_service(reservation, db, current_user.username)

# User: get their own reservation
@router.get("/{reservation_id}", response_model=ReservationResponse)
def get_reservation(
    reservation_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_reservation_service(reservation_id, db, current_user)

# Admin-only: delete any reservation
@router.delete("/{reservation_id}", response_model=ReservationResponse)
def delete_reservation(
    reservation_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin")) #que l admin peut supprimer une réservation
):
    return delete_reservation_service(reservation_id, db)

# User: cancel their own reservation
@router.patch("/{reservation_id}/cancel")
def cancel_reservation(
    reservation_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user) # que l utilisateur peut annuler sa propre réservation
):
    return cancel_reservation_service(reservation_id, db)
