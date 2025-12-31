import pytest
from datetime import datetime

AVAILABILITY_URL = "/availability/"

@pytest.mark.asyncio
async def test_create_availability(async_client):
    # Login first to get token
    login_resp = await async_client.post("/auth/login", json={
        "email": "doc1@example.com",
        "password": "password123"
    })
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = await async_client.post(AVAILABILITY_URL, json={
        "date": "2025-12-31",
        "start_time": "09:00:00",
        "end_time": "12:00:00"
    }, headers=headers)
    
    assert response.status_code == 200
    data = response.json()
    assert data["date"] == "2025-12-31"
