from sqlalchemy import select, and_, or_
from app.models import appointment
from app.models.appointment import Appointment
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date, time

class AppointmentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, appointment: Appointment):
        self.session.add(appointment)
        await self.session.commit()
        await self.session.refresh(appointment)
        return appointment

    async def check_overlap(self, doctor_id: int, date_: date, start_time: time, end_time: time):
        query = select(Appointment).where(
            Appointment.doctor_id == doctor_id,
            Appointment.date == date_,
            or_(
                and_(Appointment.start_time <= start_time, Appointment.end_time > start_time),
                and_(Appointment.start_time < end_time, Appointment.end_time >= end_time),
                and_(Appointment.start_time >= start_time, Appointment.end_time <= end_time)
            )
        )
        result = await self.session.execute(query)
        return result.scalars().all()

    async def delete_appointment(self, appointment_id: int, patient_id: int):
        query = select(Appointment).where(Appointment.id == appointment_id, Appointment.patient_id == patient_id)
        result = await self.session.execute(query)
        appointment = result.scalar_one_or_none()
        if not appointment:
            return None
        await self.session.delete(appointment)
        await self.session.commit()
        return appointment