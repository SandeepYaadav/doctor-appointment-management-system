from sqlalchemy import select, and_, or_
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.availability import Availability
from sqlalchemy import select
from app.models.availability import Availability

class AvailabilityRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, availability: Availability) -> Availability:
        self.session.add(availability)
        await self.session.commit()
        await self.session.refresh(availability)
        return availability

    async def list_by_doctor(self, doctor_id: int):
        result = await self.session.execute(
            select(Availability).where(Availability.doctor_id == doctor_id)
        )
        return result.scalars().all()

    async def check_overlap(self, doctor_id: int, date_, start_time, end_time):
        result = await self.session.execute(
            select(Availability).where(
                Availability.doctor_id == doctor_id,
                Availability.date == date_,
                or_(
                    and_(
                        Availability.start_time <= start_time,
                        Availability.end_time > start_time,
                    ),
                    and_(
                        Availability.start_time < end_time,
                        Availability.end_time >= end_time,
                    ),
                ),
            )
        )
        return result.scalars().first()
    
    async def get_availability(self, doctor_id: int):
        query = select(Availability).where(Availability.doctor_id == doctor_id)
        result = await self.session.execute(query)
        return result.scalars().all()