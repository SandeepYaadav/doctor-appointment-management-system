import enum
from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
#from app.models.availability import Availability
from sqlalchemy.orm import relationship

class UserRole(str, enum.Enum):
    DOCTOR = "DOCTOR"
    PATIENT = "PATIENT"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(255), unique=True, index=True, nullable=False
    )
    password_hash: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    appointments: Mapped[list["Appointment"]] = relationship(
    "Appointment", back_populates="patient", cascade="all, delete-orphan"
    )
    availabilities: Mapped[list["Availability"]] = relationship(
        "Availability", back_populates="doctor", cascade="all, delete-orphan"
    )
