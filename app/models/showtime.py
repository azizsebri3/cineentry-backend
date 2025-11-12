from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base


class Showtime(Base):
    __tablename__ = "showtimes"
    
    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id", ondelete="CASCADE"), nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)
    hall_number = Column(String)
    capacity = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    
    
    #ici je fais la relation vers movie
    movie = relationship("Movie", back_populates="showtimes")
    
    #ici je fais la relation entre showtime vers reservation
    reservations = relationship("Reservation", back_populates="showtime", cascade="all, delete")

    
    def __repr__(self):
        return f"<Showtime {self.start_time} for movie {self.movie_id}>"