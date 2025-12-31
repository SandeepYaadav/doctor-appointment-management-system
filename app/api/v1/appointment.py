from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.appointment import CreateAppointmentRequest, AppointmentResponse
from app.services.appointment_service import AppointmentService
from app.repositories.appointment_repository import AppointmentRepository
from app.db.session import get_session
#from app.api.dependencies.auth import get_current_user
from app.models.user import UserRole, User
from app.core.dependencies import get_current_user

router = APIRouter(tags=["Appointments"])

@router.post("/", response_model=AppointmentResponse)
async def create_appointment(
    request: CreateAppointmentRequest,
    session: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.PATIENT:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only patients can book appointments")
    
    repo = AppointmentRepository(session)
    service = AppointmentService(repo)

    try:
        appointment = await service.book_appointment(
            patient_id=current_user.id,
            doctor_id=request.doctor_id,
            date_=request.date,
            start_time=request.start_time,
            end_time=request.end_time
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return appointment


@router.delete("/{appointment_id}", response_model=AppointmentResponse)
async def cancel_appointment(
    appointment_id: int = Path(...),
    session: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.PATIENT:
        raise HTTPException(status_code=403, detail="Only patients can cancel appointments")
    
    repo = AppointmentRepository(session)
    service = AppointmentService(repo)
    try:
        return await service.cancel_appointment(appointment_id, current_user.id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))