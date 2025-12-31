from datetime import date, time
from pydantic import BaseModel

class AvailabilityCreate(BaseModel):
    date: date
    start_time: time
    end_time: time

class AvailabilityResponse(AvailabilityCreate):
    id: int
    doctor_id: int

    class Config:
        orm_mode = True
