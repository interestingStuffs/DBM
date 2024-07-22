# tests/test_event.py
import pytest
from httpx import AsyncClient
from app.main import app
from datetime import datetime

@pytest.fixture
def anyio_backend():
    return 'asyncio'

@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

# Test creating an event
@pytest.mark.anyio
async def test_create_event(client: AsyncClient):
    event_data = {
        "name": "Test Event",
        "description": {
            "en": "A test event",
            "fr": "Un événement test"
        },
        "location": "Test Location",
        "start_time": datetime(2024, 7, 21, 10, 0, 0).isoformat(),
        "end_time": datetime(2024, 7, 21, 12, 0, 0).isoformat()
    }
    response = await client.post("/api/v1/events/", json=event_data)
    assert response.status_code == 200
    
    # Print the response content for debugging
    print("Create response:", response.json())
    
    assert "_id" in response.json()
    assert response.json()["name"] == event_data["name"]

# Test retrieving an event
@pytest.mark.anyio
async def test_get_event(client: AsyncClient):
    # First, create an event to ensure there's something to retrieve
    event_data = {
        "name": "Test Event for retrieval",
        "description": {
            "en": "A test event",
            "fr": "Un événement test pour retrieve"
        },
        "location": "Test Location",
        "start_time": datetime(2024, 7, 21, 10, 0, 0).isoformat(),
        "end_time": datetime(2024, 7, 21, 12, 0, 0).isoformat()
    }
    create_response = await client.post("/api/v1/events/", json=event_data)
    
    # Print the create response for debugging
    print("Create response:", create_response.json())
    
    assert create_response.status_code == 200
    created_event = create_response.json()
    
    # Check for '_id' field
    assert "_id" in created_event
    event_id = created_event["_id"]
    
    # Retrieve the event
    get_response = await client.get(f"/api/v1/events/{event_id}")
    assert get_response.status_code == 200
    retrieved_event = get_response.json()
    
    # Assert the retrieved event matches the created event
    assert retrieved_event["name"] == event_data["name"]
    assert retrieved_event["description"] == event_data["description"]
    assert retrieved_event["location"] == event_data["location"]
    assert retrieved_event["start_time"] == event_data["start_time"]
    assert retrieved_event["end_time"] == event_data["end_time"]
