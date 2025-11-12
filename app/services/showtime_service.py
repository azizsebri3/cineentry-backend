from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.showtime import Showtime as ShowtimeModel
from app.models.reservation import Reservation as ReservationModel
from app.utils.seats import generate_seats


def get_showtimes_service(skip: int, limit: int, db: Session):
    showtimes = db.query(ShowtimeModel).offset(skip).limit(limit).all()

    if not showtimes:
        raise HTTPException(status_code=404, detail="Aucun showtime trouvé !")

    return showtimes


def create_showtime_service(showtime_data, db: Session):
    db_showtime = ShowtimeModel(**showtime_data.model_dump())
    db.add(db_showtime)
    db.commit()
    db.refresh(db_showtime)
    return db_showtime


def get_showtimes_by_movie_service(movie_id: int, db: Session):
    showtimes = db.query(ShowtimeModel).filter(
        ShowtimeModel.movie_id == movie_id
    ).all()

    if not showtimes:
        raise HTTPException(
            status_code=404, 
            detail=f"Aucun showtime trouvé pour le film {movie_id}"
        )

    return showtimes


def delete_showtime_service(showtime_id: int, db: Session):
    showtime = db.query(ShowtimeModel).filter(
        ShowtimeModel.id == showtime_id
    ).first()

    if not showtime:
        raise HTTPException(
            status_code=404, 
            detail="Showtime not found to delete it"
        )

    db.delete(showtime)
    db.commit()

    return showtime


def get_available_seats_service(showtime_id: int, db: Session):
    # on Vérifie que le showtime existe ----------
    showtime = db.query(ShowtimeModel).filter(ShowtimeModel.id == showtime_id).first()
    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")
    
    if showtime.capacity <= 0:
        raise HTTPException(status_code=400, detail="Showtime has no seats configured")

    # je fais la Génération de tous les sièges possibles --------
    all_seats = generate_seats(showtime.capacity)

    # Récupérer les sièges déjà réservés ---------
    reserved = db.query(ReservationModel.seat_number).filter(
        ReservationModel.showtime_id == showtime_id,
        ReservationModel.status == "confirmed"
    ).all()

    reserved_seats = [r[0] for r in reserved]

    # Calculer les sièges disponibles
    available_seats = [s for s in all_seats if s not in reserved_seats]

    return {
        "showtime_id": showtime_id,
        "available_seats": sorted(available_seats,reverse=False),
        "capacity": showtime.capacity,
        "available_count": len(available_seats),
        "reserved_count": len(reserved_seats)
    }