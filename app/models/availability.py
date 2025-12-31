from datetime import date, time
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.models.user import User

class Availability(Base):
    __tablename__ = "availabilities"

    id: Mapped[int] = mapped_column(primary_key=True)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    availability_date: Mapped[date] = mapped_column(nullable=False)       
    start_time: Mapped[time] = mapped_column(nullable=False)  
    end_time: Mapped[time] = mapped_column(nullable=False)   

    doctor: Mapped["User"] = relationship("User", back_populates="availabilities")
