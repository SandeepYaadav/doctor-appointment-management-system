from app.repositories.appointment_repository import AppointmentRepository
from app.models.appointment import Appointment
from datetime import date, time

class AppointmentService:
    def __init__(self, repo: AppointmentRepository):
        self.repo = repo

    async def book_appointment(self, patient_id: int, doctor_id: int, date_: date, start_time: time, end_time: time):
        # Check for overlap
        overlap = await self.repo.check_overlap(doctor_id, date_, start_time, end_time)
        if overlap:
            raise ValueError("Appointment overlaps with existing one")

        appointment = Appointment(
            patient_id=patient_id,
            doctor_id=doctor_id,
            date=date_,
            start_time=start_time,
            end_time=end_time
        )
        return await self.repo.create(appointment)

    async def cancel_appointment(self, appointment_id: int, patient_id: int):
        appointment = await self.repo.delete_appointment(appointment_id, patient_id)
        if not appointment:
            raise ValueError("Appointment not found or not yours")
        return appointment