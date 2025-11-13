from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from app.models.reservation import Reservation as ReservationModel
from app.models.showtime import Showtime as ShowtimeModel
from ..utils.seats import generate_seats


def get_all_reservations(db: Session):
    return db.query(ReservationModel).all()


def create_reservation_service(reservation_data, db: Session):
    showtime = db.query(ShowtimeModel).filter(
        ShowtimeModel.id == reservation_data.showtime_id
    ).first()

    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")

    if showtime.capacity <= 0:
        raise HTTPException(status_code=400, detail="Showtime has no seats configured")

    #ici je vais generer la salle complete (l'utilisation de la fonction generate_seats )
    all_seats = generate_seats(showtime.capacity)
    #je verife si la siege dispo ou pas
    if reservation_data.seat_number not in all_seats:
        raise HTTPException(status_code=400, detail="Seat does not exist in this hall")
    
    #ici je vais checker si le siege est deja reservé ou pas (dans la filtre je fais la jointure de pk et fk et il faut la statut etre confirmé)
    reserved = db.query(ReservationModel).filter(
        ReservationModel.showtime_id == reservation_data.showtime_id,
        ReservationModel.seat_number == reservation_data.seat_number,
        ReservationModel.status == "confirmed"
    ).first()
    
    if reserved:
        raise HTTPException(status_code=400, detail="Seat already reserved") 
    
    
    db_reservation = ReservationModel(**reservation_data.model_dump())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)

    return db_reservation


def get_reservation_service(reservation_id: int, db: Session):
    reservation = db.query(ReservationModel).filter(
        ReservationModel.id == reservation_id
    ).first()

    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")

    return reservation


def delete_reservation_service(reservation_id: int, db: Session):
    reservation = db.query(ReservationModel).filter(
        ReservationModel.id == reservation_id
    ).first()

    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")

    db.delete(reservation)
    db.commit()
    return reservation



def cancel_reservation_service(reservation_id: int, db: Session):
    # 1️⃣ Récupérer la réservation
    reservation = db.query(ReservationModel).filter(
        ReservationModel.id == reservation_id
    ).first()

    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")

    # 2️⃣ Vérifier que le showtime est à venir
    showtime = db.query(ShowtimeModel).filter(
        ShowtimeModel.id == reservation.showtime_id
    ).first()

    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")

    # On compare les dates (UTC)
    if showtime.start_time <= datetime.now(timezone.utc):
        raise HTTPException(status_code=400, detail="Cannot cancel past reservations")

    # 3️⃣ Mettre à jour le statut
    reservation.status = "cancelled"
    db.commit()
    db.refresh(reservation)

    return {"message": "Reservation cancelled successfully", "reservation": reservation}
