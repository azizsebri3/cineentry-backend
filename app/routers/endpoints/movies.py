from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from datetime import date
from app.models.movie import Movie as MovieModel
from ...database import get_db
from ...schemas.movie import Movie, MovieCreate
from ...services.movies_service import (
    get_movies_service,
    create_movie_service,
    get_movie_service,
    update_movie_service,
    delete_movie_service,
    get_movies_by_showtime_date_service
)

router = APIRouter()


@router.get("/", response_model=List[Movie])
def get_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_movies_service(skip, limit, db)


@router.post("/", response_model=Movie)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    return create_movie_service(movie, db)


@router.get("/{movie_id}", response_model=Movie)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    return get_movie_service(movie_id, db)


@router.patch("/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, movie: MovieCreate, db: Session = Depends(get_db)):
    return update_movie_service(movie_id, movie, db)


@router.delete("/{movie_id}", response_model=Movie)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    return delete_movie_service(movie_id, db)

from sqlalchemy import cast, Date
from app.models.showtime import Showtime as ShowtimeModel
from app.models.movie import Movie as MovieModel

@router.get("/by-date/{showtime_date}", response_model=List[Movie])
def get_movies_by_showtime_date(
                showtime_date: date,
                db: Session = Depends(get_db)):
    
    return get_movies_by_showtime_date_service(showtime_date, db)

