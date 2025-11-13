from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.core.security import require_role
from app.core.deps import get_current_user
from app.schemas.showtime import Showtime, ShowtimeCreate
from app.services.showtime_service import (
    get_available_seats_service,
    get_showtimes_service,
    create_showtime_service,
    get_showtimes_by_movie_service,
    delete_showtime_service
)

router = APIRouter(prefix="/showtimes", tags=["Showtimes"])

@router.get("/", response_model=List[Showtime])
def get_showtimes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Public
    return get_showtimes_service(skip, limit, db)

@router.post("/", response_model=Showtime)
def create_showtime(
    showtime: ShowtimeCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    return create_showtime_service(showtime, db)

@router.get("/{movie_id}/showtimes", response_model=List[Showtime])
def get_movie_showtimes(movie_id: int, db: Session = Depends(get_db)):
    # Public
    return get_showtimes_by_movie_service(movie_id, db)

@router.delete("/{showtime_id}", response_model=Showtime)
def delete_showtime(
    showtime_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    return delete_showtime_service(showtime_id, db)

@router.get("/{showtime_id}/available-seats")
def get_available_seats(showtime_id: int, db: Session = Depends(get_db)):
    # Public
    return get_available_seats_service(showtime_id, db)
