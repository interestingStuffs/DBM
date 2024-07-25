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

# Test retrieving all events
@pytest.mark.anyio
async def test_list_events(client: AsyncClient):
    # First, create a couple of events to ensure there's something to list
    event_data1 = {
        "name": "Test Event 1",
        "description": {"en": "First test event", "fr": "Premier événement test"},
        "location": "Location 1",
        "start_time": datetime(2024, 7, 21, 10, 0, 0).isoformat(),
        "end_time": datetime(2024, 7, 21, 12, 0, 0).isoformat()
    }
    event_data2 = {
        "name": "Test Event 2",
        "description": {"en": "Second test event", "fr": "Deuxième événement test"},
        "location": "Location 2",
        "start_time": datetime(2024, 7, 22, 10, 0, 0).isoformat(),
        "end_time": datetime(2024, 7, 22, 12, 0, 0).isoformat()
    }
    await client.post("/api/v1/events/", json=event_data1)
    await client.post("/api/v1/events/", json=event_data2)
    
    # List all events
    list_response = await client.get("/api/v1/events/")
    assert list_response.status_code == 200
    events = list_response.json()
    
    # Print the response content for debugging
    print("List response:", events)
    
    # Check if at least two events are returned
    assert len(events) >= 2

    # Validate the structure of the response
    for event in events:
        assert "name" in event
        assert "description" in event
        assert "location" in event
        assert "start_time" in event
        assert "end_time" in event

# Test retrieving events by date range
@pytest.mark.anyio
async def test_get_events_by_date_range(client: AsyncClient):
    # Create events within and outside the date range
    event_data1 = {
        "name": "Event Within Range",
        "description": {"en": "An event within the range", "fr": "Un événement dans la plage"},
        "location": "Location A",
        "start_time": datetime(2024, 7, 20, 10, 0, 0).isoformat(),
        "end_time": datetime(2024, 7, 20, 12, 0, 0).isoformat()
    }
    event_data2 = {
        "name": "Event Outside Range",
        "description": {"en": "An event outside the range", "fr": "Un événement en dehors de la plage"},
        "location": "Location B",
        "start_time": datetime(2024, 7, 25, 10, 0, 0).isoformat(),
        "end_time": datetime(2024, 7, 25, 12, 0, 0).isoformat()
    }
    await client.post("/api/v1/events/", json=event_data1)
    await client.post("/api/v1/events/", json=event_data2)
    
    # Define the date range for the test
    start_date = datetime(2024, 7, 19).isoformat()
    end_date = datetime(2024, 7, 21).isoformat()
    
    # Retrieve events by date range
    range_response = await client.get(f"/api/v1/events/range?start_date={start_date}&end_date={end_date}")
    assert range_response.status_code == 200
    events_in_range = range_response.json()
    
    # Print the response content for debugging
    print("Range response:", events_in_range)
    
    # Assert that the event within range is returned with expected fields
    assert any(event["id"] and event["title"] == "Event Within Range" and event["date"] == "2024-07-20T10:00:00" for event in events_in_range)
    
    # Assert that the event outside range is not returned
    assert not any(event["id"] and event["title"] == "Event Outside Range" for event in events_in_range)
