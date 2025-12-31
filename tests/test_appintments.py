import pytest

APPOINTMENTS_URL = "/appointments/"

@pytest.mark.asyncio
async def test_book_appointment(async_client):
    # Login as patient
    login_resp = await async_client.post("/auth/register", json={
        "email": "patient1@example.com",
        "password": "patientpass",
        "name": "Patient One",
        "role": "PATIENT"
    })
    
    login_resp = await async_client.post("/auth/login", json={
        "email": "patient1@example.com",
        "password": "patientpass"
    })
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Book appointment with doctor id 1
    response = await async_client.post(APPOINTMENTS_URL, json={
        "doctor_id": 1,
        "date": "2025-12-31",
        "start_time": "10:00:00",
        "end_time": "11:00:00"
    }, headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert data["doctor_id"] == 1
    assert data["patient_id"] > 0
