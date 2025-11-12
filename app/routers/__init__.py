from fastapi import APIRouter
from .endpoints import movies, showtime, reservation

router = APIRouter()
router.include_router(movies.router, prefix="/movies", tags=["Movies"])
router.include_router(showtime.router, prefix="/showtimes", tags=["Showtimes"])
router.include_router(reservation.router, prefix="/reservations", tags=["Reservations"])
