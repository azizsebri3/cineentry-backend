from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False)
    showtime_id = Column(Integer, ForeignKey("showtimes.id", ondelete="CASCADE"), nullable=False)
    seat_number = Column(String, nullable=False)
    status = Column(String, default="confirmed")
    created_at = Column(DateTime(timezone=True), server_default=func.now())



    showtime = relationship("Showtime", back_populates="reservations")
