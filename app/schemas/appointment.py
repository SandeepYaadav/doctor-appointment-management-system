from datetime import date, time
from pydantic import BaseModel

class CreateAppointmentRequest(BaseModel):
    doctor_id: int
    date: date
    start_time: time
    end_time: time

class AppointmentResponse(BaseModel):
    id: int
    doctor_id: int
    patient_id: int
    date: date
    start_time: time
    end_time: time

    class Config:
        orm_mode = True
