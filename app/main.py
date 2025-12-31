from fastapi import FastAPI
from app.api.v1.auth import router as auth_router
from app.api.v1.availability import router as availability_router
from app.api.v1.doctor import router as doctors_router
from app.api.v1.appointment import router as appointments_router
from app.db.init_db import init_db

app = FastAPI(title="Doctor Appointment API")


@app.on_event("startup")
async def on_startup():
    await init_db()


# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(availability_router, prefix="/availability", tags=["Availability"])
app.include_router(doctors_router, prefix="/doctors", tags=["Doctors"])
app.include_router(appointments_router, prefix="/appointments", tags=["Appointments"])
