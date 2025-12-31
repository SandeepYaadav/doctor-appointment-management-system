import pytest
from httpx import AsyncClient
from app.main import app
from app.db.session import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.init_db import init_db

@pytest.fixture(scope="session")
async def async_client():
    # Initialize database before tests
    await init_db()

    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

# Optionally, override DB session if using a test database
@pytest.fixture
async def db_session():
    async for session in get_session():
        yield session
