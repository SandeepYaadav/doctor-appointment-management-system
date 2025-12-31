import pytest

REGISTER_URL = "/auth/register"
LOGIN_URL = "/auth/login"

@pytest.mark.asyncio
async def test_register_login(async_client):
    # Register a new doctor
    response = await async_client.post(REGISTER_URL, json={
        "email": "doc1@example.com",
        "password": "password123",
        "name": "Dr One",
        "role": "DOCTOR"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "doc1@example.com"

    # Login with the same doctor
    response = await async_client.post(LOGIN_URL, json={
        "email": "doc1@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
