from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.db.session import get_session
from app.schemas.user import UserResponse
from app.repositories.availability_repository import AvailabilityRepository
from app.services.availability_service import AvailabilityService
from app.schemas.availability import AvailabilityResponse

router = APIRouter(tags=["Doctors"])

@router.get("/", response_model=list[UserResponse])
async def list_doctors(session: AsyncSession = Depends(get_session)):
    repo = UserRepository(session)
    service = UserService(repo)
    return await service.list_doctors()


@router.get("/{doctor_id}/availability", response_model=list[AvailabilityResponse])
async def doctor_availability(doctor_id: int, session: AsyncSession = Depends(get_session)):
    repo = AvailabilityRepository(session)
    service = AvailabilityService(repo)
    return await service.list_availability(doctor_id)