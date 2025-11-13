from fastapi import APIRouter
from .endpoints import movies, showtime, reservation, user

router = APIRouter()
router.include_router(movies.router, prefix="/movies", tags=["Movies"])
router.include_router(showtime.router, prefix="/showtimes", tags=["Showtimes"])
router.include_router(reservation.router, prefix="/reservations", tags=["Reservations"])
router.include_router(user.router, prefix="/users", tags=["Users"])
router.include_router(user.router, prefix="/auth", tags=["Authentication"])
