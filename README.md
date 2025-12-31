Doctor Appointment Management System API

Version: 0.1.0
Tech Stack: Python 3.12, FastAPI, PostgreSQL, SQLAlchemy (Async), Pydantic, JWT, Pytest

Table of Contents
Project Overview
Features
Tech Stack
Setup Instructions
API Endpoints
Authentication & RBAC
Testing

Project Overview
This is a Doctor Appointment Management System API built with FastAPI. It allows:
Doctors to define their available time slots.
Patients to view availability and book appointments.
Full JWT-based authentication and role-based access control (RBAC).
The API is production-ready and follows a Service / Repository pattern for clean architecture.

Features
User registration and login (Doctor/Patient)
JWT authentication for secure API access
Doctor availability management
Appointment booking and cancellation
RBAC enforcement (Doctors vs Patients)
Swagger/OpenAPI documentation

Tech Stack
Python 3.12 – Backend language
FastAPI – Web framework
PostgreSQL – Database (can be run via Docker)
SQLAlchemy / Async – ORM
Pydantic – Data validation and serialization
JWT – Authentication
Pytest – Testing

Setup Instructions
1. Clone the repository
   git clone https://github.com/SandeepYaadav/doctor-appointment-management-system
   cd doctor-appointment-management-system

2. Create a .env file in the root folder:
   DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/doctor_db
   SECRET_KEY=your_jwt_secret_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=60

3. Run PostgreSQL via Docker
   docker run --name doctor_postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -e POSTGRES_DB=doctor_db -p 5432:5432 -d postgres:15

4. Install dependencies
   pip install -r requirements.txt

5. Run the app
   uvicorn app.main:app --reload

Open Swagger docs: http://localhost:8000/docs
Open OpenAPI JSON: http://localhost:8000/openapi.json


Authentication & RBAC Design
    JWT Authentication:
        Access token is issued after login.
        Token must be included in the Authorization header as Bearer <token>.

    Roles:
        DOCTOR – Can set availability and view appointments.
        PATIENT – Can book and cancel appointments.

    RBAC Enforcement:
        Routes check the user role to ensure proper access.
        Example: Only PATIENT role can access /appointments/ endpoints.

Testing
    Run the Pytest test suite:
    pytest -v

Tests cover:
    Auth (register/login)
    Availability creation
    Doctor listing
    Appointment booking and cancellation
    RBAC enforcement and validation errors

Notes
    Passwords are hashed using bcrypt.
    All data validation is done via Pydantic.
    Async SQLAlchemy ensures high performance and scalability.
    Overlapping appointments are prevented.    