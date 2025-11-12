from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.movie import Movie as MovieModel
from app.models.showtime import Showtime as ShowtimeModel


def get_movies_service(skip: int, limit: int, db: Session):
    return db.query(MovieModel).offset(skip).limit(limit).all()


def create_movie_service(movie_data, db: Session):
    db_movie = MovieModel(**movie_data.model_dump())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def get_movie_service(movie_id: int, db: Session):
    movie = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    if movie is None:
        raise HTTPException(status_code=404, detail="Film non trouvé")
    return movie


def update_movie_service(movie_id: int, movie_data, db: Session):
    db_movie = db.query(MovieModel).filter(MovieModel.id == movie_id).first()

    if db_movie is None:
        raise HTTPException(status_code=404, detail="Film non trouvé")

    # Update champ par champ
    for key, value in movie_data.model_dump().items():
        setattr(db_movie, key, value)

    db.commit()
    db.refresh(db_movie)
    return db_movie


def delete_movie_service(movie_id: int, db: Session):
    movie = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    if movie is None:
        raise HTTPException(status_code=404, detail="Film non trouvé")

    db.delete(movie)
    db.commit()
    return movie

def get_movies_by_showtime_date_service(showtime_date, db: Session):
    if not showtime_date:
        return db.query(MovieModel).all()
    
    if showtime_date:
        q = (
            db.query(MovieModel)
            .join(MovieModel.showtimes)
            .filter(func.date(ShowtimeModel.start_time) == showtime_date)
            .distinct()
        )
        movies = q.all()
    if showtime_date and not movies:
        raise HTTPException(status_code=404, detail="Aucun film trouvé pour la date spécifiée")
    else:
        return movies