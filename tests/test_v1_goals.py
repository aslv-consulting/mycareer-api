"""
test_v1_goals.py

This module contains tests for the API endpoints defined in v1_goals.py.

Fixtures:
    client_fixture: Creates a TestClient for the FastAPI app.

Functions:
    initialize_goal: 
        Initializes a test goal in the database.

    test_get_goals: 
        Tests the get_goals endpoint.

    test_get_existing_goal:
        Tests the get_goal endpoint with an existing goal.

    test_get_non_existing_goal:
        Tests the get_goal endpoint with a non-existing goal.

    test_create_goal: 
        Tests the create_goal endpoint with all fields set.
    
    test_create_goal_without_optional_fields: 
        Tests the create_goal endpoint without optional fields.
    
    test_create_goal_without_fields: 
        Tests the create_goal endpoint without fields.

    test_create_goal_with_empty_name: 
        Tests the create_goal endpoint with an empty name.
    
    test_create_goal_with_none_name: 
        Tests the create_goal endpoint with an None name.

    test_create_goal_with_none_description: 
        Tests the create_goal endpoint with a None description.
    
    test_create_goal_with_empty_description: 
        Tests the create_goal endpoint with an empty description.

    test_create_goal_with_empty_status: 
        Tests the create_goal endpoint with an empty status.

    test_create_goal_with_none_status: 
        Tests the create_goal endpoint with a None status.

    test_create_goal_with_bad_status: 
        Tests the create_goal endpoint with bad status.

    test_create_goal_with_empty_priority: 
        Tests the create_goal endpoint with an empty priority.

    test_create_goal_with_none_priority: 
        Tests the create_goal endpoint with a None priority.
    
    test_create_goal_with_bad_priority: 
        Tests the create_goal endpoint with bad priority.

    test_create_goal_with_empty_due_date: 
        Tests the create_goal endpoint with an empty due date.
    
    test_create_goal_with_none_due_date: 
        Tests the create_goal endpoint with a None due date.

    test_update_goal: 
        Tests the update_goal endpoint with all fields set.

    test_update_non_existing_goal:
        Tests the update_goal endpoint with a non-existing goal.
    
    test_update_goal_without_optional_fields: 
        Tests the update_goal endpoint without optional fields.
    
    test_update_goal_without_fields: 
        Tests the update_goal endpoint without fields.

    test_update_goal_with_empty_name: 
        Tests the update_goal endpoint with an empty name.
    
    test_update_goal_with_none_name: 
        Tests the update_goal endpoint with an None name.

    test_update_goal_with_none_description: 
        Tests the update_goal endpoint with a None description.
    
    test_update_goal_with_empty_description: 
        Tests the update_goal endpoint with an empty description.

    test_update_goal_with_empty_status: 
        Tests the update_goal endpoint with an empty status.

    test_update_goal_with_none_status: 
        Tests the update_goal endpoint with a None status.

    test_update_goal_with_bad_status: 
        Tests the update_goal endpoint with bad status.

    test_update_goal_with_empty_priority: 
        Tests the update_goal endpoint with an empty priority.

    test_update_goal_with_none_priority: 
        Tests the update_goal endpoint with a None priority.
    
    test_update_goal_with_bad_priority: 
        Tests the update_goal endpoint with bad priority.

    test_update_goal_with_empty_due_date: 
        Tests the update_goal endpoint with an empty due date.
    
    test_update_goal_with_none_due_date: 
        Tests the update_goal endpoint with a None due date.

    test_delete_existing_goal:
        Tests the delete_goal endpoint with an existing goal.

    test_delete_non_existing_goal:
        Tests the delete_goal endpoint with a non-existing goal.
"""

from typing import Generator
import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel
from mycareer.main import app
from mycareer.models import Goal
from mycareer.database import engine, get_session

@pytest.fixture(name="client")
def client_fixture() -> Generator[TestClient, None, None]:
    """Fixture to create a TestClient for the FastAPI app.

    This fixture sets up the database, creates a TestClient for the FastAPI app,
    and tears down the database after the test.

    Yields:
        TestClient: The test client for making requests to the FastAPI app.
    """
    SQLModel.metadata.create_all(engine)
    with TestClient(app) as client:
        yield client
    SQLModel.metadata.drop_all(engine)

def initialize_goal() -> None:
    """Initializes a test goal in the database.

    This function creates and commits a test goal to the database.
    """
    with next(get_session()) as session:
        goal = Goal(
            name="Test Goal",
            description="A test goal",
            status="to refine",
            priority="medium"
        )
        session.add(goal)
        session.commit()
        session.refresh(goal)
        return goal

def test_get_goals(client: TestClient) -> None:
    """Test the get_goals endpoint.

    This test checks if the get_goals endpoint returns a list of goals.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Initialize a test goal
    initialize_goal()

    # Make a request to the get_goals endpoint
    response = client.get("/v1/goals")

    # Check the response
    assert response.status_code == 200
    goals = response.json()
    assert len(goals) == 1
    assert goals[0]["name"] == "Test Goal"
    assert goals[0]["description"] == "A test goal"
    assert goals[0]["status"] == "to refine"
    assert goals[0]["priority"] == "medium"

def test_get_existing_goal(client: TestClient) -> None:
    """Test the get_goal endpoint with an existing goal.

    This test checks if the get_goal endpoint returns the goal with the given ID.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Initialize a test goal
    goal = initialize_goal()

    # Make a request to the get_goal endpoint
    response = client.get(f"/v1/goals/{goal.id}")

    # Check the response
    assert response.status_code == 200
    goal_data = response.json()
    assert goal_data["name"] == "Test Goal"
    assert goal_data["description"] == "A test goal"
    assert goal_data["status"] == "to refine"
    assert goal_data["priority"] == "medium"

def test_get_non_existing_goal(client: TestClient) -> None:
    """Test the get_goal endpoint with a non-existing goal.

    This test checks if the get_goal endpoint returns a 404 status code
    when the goal does not exist.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Make a request to the delete_goal endpoint with a non-existing goal ID
    response = client.get("/v1/goals/999")

    # Check the response
    assert response.status_code == 404
    assert response.json() == {"detail": "Goal not found"}

def test_create_goal(client: TestClient) -> None:
    """Test the create_goal endpoint with all fields set.

    This test checks if the create_goal endpoint correctly creates a new goal
    when all fields are provided.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    goal_data = {
        "name": "New Goal",
        "description": "A new goal",
        "status": "to refine",
        "priority": "medium",
        "due_date": "2024-12-31T23:59:59"
    }

    # Make a request to the create_goal endpoint
    response = client.post("/v1/goals", json=goal_data)

    # Check the response
    assert response.status_code == 200
    created_goal = response.json()
    assert created_goal["name"] == "New Goal"
    assert created_goal["description"] == "A new goal"
    assert created_goal["status"] == "to refine"
    assert created_goal["priority"] == "medium"
    assert created_goal["due_date"] == "2024-12-31T23:59:59"

    # Verify the goal was added to the database
    with next(get_session()) as session:
        goal_in_db = session.get(Goal, created_goal["id"])
        assert goal_in_db is not None
        assert goal_in_db.name == "New Goal"
        assert goal_in_db.description == "A new goal"
        assert goal_in_db.status == "to refine"
        assert goal_in_db.priority == "medium"
        assert goal_in_db.due_date.isoformat() == "2024-12-31T23:59:59"

def test_create_goal_without_optional_fields(client: TestClient) -> None:
    """Test the create_goal endpoint without optional fields.

    This test checks if the create_goal endpoint correctly creates a new goal
    when only the required fields are provided.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    goal_data = {
        "name": "New Goal"
    }

    # Make a request to the create_goal endpoint
    response = client.post("/v1/goals", json=goal_data)

    # Check the response
    assert response.status_code == 200
    created_goal = response.json()
    assert created_goal["name"] == "New Goal"
    assert created_goal["description"] is None
    assert created_goal["status"] == "to refine"
    assert created_goal["priority"] == "medium"
    assert created_goal["due_date"] is None

def test_create_goal_without_fields(client: TestClient) -> None:
    """Test the create_goal endpoint without fields.

    This test checks if the create_goal endpoint returns a 422 status code
    when the all fields are missing.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    goal_data = {}

    # Make a request to the create_goal endpoint
    response = client.post("/v1/goals", json=goal_data)

    # Check the response
    assert response.status_code == 422

def test_create_goal_empty_name(client: TestClient) -> None:
    """Test the create_goal endpoint with an empty name.

    This test checks if the create_goal endpoint returns a 422 status code
    when the name field is empty.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    goal_data = {
        "name": ""
    }

    # Make a request to the create_goal endpoint
    response = client.post("/v1/goals", json=goal_data)

    # Check the response
    assert response.status_code == 422

def test_create_goal_with_none_name(client: TestClient) -> None:
    """Test the create_goal endpoint with None name.

    This test checks if the create_goal endpoint returns a 422 status code
    when the name field is None.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    goal_data = {
        "name": None
    }

    # Make a request to the create_goal endpoint
    response = client.post("/v1/goals", json=goal_data)

    # Check the response
    assert response.status_code == 422

def test_create_goal_with_empty_description(client: TestClient) -> None:
    """Test the create_goal endpoint with an empty description.

    This test checks if the create_goal endpoint correctly creates a new goal
    when the description field is empty.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    goal_data = {
        "name": "New Goal",
        "description": ""
    }

    # Make a request to the create_goal endpoint
    response = client.post("/v1/goals", json=goal_data)

    # Check the response
    assert response.status_code == 200
    created_goal = response.json()
    assert created_goal["name"] == "New Goal"
    assert created_goal["description"] == ""
    assert created_goal["status"] == "to refine"
    assert created_goal["priority"] == "medium"
    assert created_goal["due_date"] is None

def test_create_goal_with_none_description(client: TestClient) -> None:
    """Test the create_goal endpoint with a None description.

    This test checks if the create_goal endpoint correctly creates a new goal
    when the description field is None.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    goal_data = {
        "name": "New Goal",
        "description": None
    }

    # Make a request to the create_goal endpoint
    response = client.post("/v1/goals", json=goal_data)

    # Check the response
    assert response.status_code == 200
    created_goal = response.json()
    assert created_goal["name"] == "New Goal"
    assert created_goal["description"] is None
    assert created_goal["status"] == "to refine"
    assert created_goal["priority"] == "medium"
    assert created_goal["due_date"] is None

def test_create_goal_with_empty_status(client: TestClient) -> None:
    """Test the create_goal endpoint with an empty status.

    This test checks if the create_goal endpoint returns a 422 status code
    when the status field is empty.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    goal_data = {
        "name": "New Goal",
        "status": ""
    }

    # Make a request to the create_goal endpoint
    response = client.post("/v1/goals", json=goal_data)

    # Check the response
    assert response.status_code == 422

def test_create_goal_with_none_status(client: TestClient) -> None:
    """Test the create_goal endpoint with a None status.

    This test checks if the create_goal endpoint correctly creates a new goal
    when the status field is None.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    goal_data = {
        "name": "New Goal",
        "status": None
    }

    # Make a request to the create_goal endpoint
    response = client.post("/v1/goals", json=goal_data)

    # Check the response
    assert response.status_code == 200
    created_goal = response.json()
    assert created_goal["name"] == "New Goal"
    assert created_goal["description"] is None
    assert created_goal["status"] == "to refine"
    assert created_goal["priority"] == "medium"
    assert created_goal["due_date"] is None

def test_create_goal_with_bad_status(client: TestClient) -> None:
    """Tests the create_goal endpoint with bad status.

    This test checks if the create_goal endpoint returns a 422 status code
    when the status fields has a bad value.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    goal_data = {
        "name": "New Goal",
        "status": "bad status"
    }

    # Make a request to the create_goal endpoint
    response = client.post("/v1/goals", json=goal_data)

    # Check the response
    assert response.status_code == 422

def test_create_goal_with_empty_priority(client: TestClient) -> None:
    """Test the create_goal endpoint with an empty priority.

    This test checks if the create_goal endpoint returns a 422 status code
    when the priority field is empty.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    goal_data = {
        "name": "New Goal",
        "priority": ""
    }

    # Make a request to the create_goal endpoint
    response = client.post("/v1/goals", json=goal_data)

    # Check the response
    assert response.status_code == 422

def test_create_goal_with_none_priority(client: TestClient) -> None:
    """Test the create_goal endpoint with a None priority.

    This test checks if the create_goal endpoint correctly creates a new goal
    when the priority field is None.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    goal_data = {
        "name": "New Goal",
        "priority": None
    }

    # Make a request to the create_goal endpoint
    response = client.post("/v1/goals", json=goal_data)

    # Check the response
    assert response.status_code == 200
    created_goal = response.json()
    assert created_goal["name"] == "New Goal"
    assert created_goal["description"] is None
    assert created_goal["status"] == "to refine"
    assert created_goal["priority"] == "medium"
    assert created_goal["due_date"] is None

def test_create_goal_with_bad_priority(client: TestClient) -> None:
    """Tests the create_goal endpoint with bad priority.

    This test checks if the create_goal endpoint returns a 422 status code
    when the priority fields has a bad value.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    goal_data = {
        "name": "New Goal",
        "priority": "bad priority"
    }

    # Make a request to the create_goal endpoint
    response = client.post("/v1/goals", json=goal_data)

    # Check the response
    assert response.status_code == 422

def test_create_goal_with_empty_due_date(client: TestClient) -> None:
    """Test the create_goal endpoint with an empty due date.

    This test checks if the create_goal endpoint returns a 422 status code
    when the due_date field is empty.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    goal_data = {
        "name": "New Goal",
        "due_date": ""
    }

    # Make a request to the create_goal endpoint
    response = client.post("/v1/goals", json=goal_data)

    # Check the response
    assert response.status_code == 422

def test_create_goal_with_none_due_date(client: TestClient) -> None:
    """Test the create_goal endpoint with a None due date.

    This test checks if the create_goal endpoint correctly creates a new goal
    when the due_date field is None.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    goal_data = {
        "name": "New Goal",
        "due_date": None
    }

    # Make a request to the create_goal endpoint
    response = client.post("/v1/goals", json=goal_data)

    # Check the response
    assert response.status_code == 200
    created_goal = response.json()
    assert created_goal["name"] == "New Goal"
    assert created_goal["description"] is None
    assert created_goal["status"] == "to refine"
    assert created_goal["priority"] == "medium"
    assert created_goal["due_date"] is None

def test_update_goal(client: TestClient) -> None:
    """Test the update_goal endpoint with all fields set.

    This test checks if the update_goal endpoint correctly updates an existing goal
    when all fields are provided.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Initialize a test goal
    goal = initialize_goal()

    updated_goal_data = {
        "name": "Updated Goal",
        "description": "An updated goal",
        "status": "in progress",
        "priority": "high",
        "due_date": "2025-12-31T23:59:59"
    }

    # Make a request to the update_goal endpoint
    response = client.put(f"/v1/goals/{goal.id}", json=updated_goal_data)

    # Check the response
    assert response.status_code == 200
    updated_goal = response.json()
    assert updated_goal["name"] == "Updated Goal"
    assert updated_goal["description"] == "An updated goal"
    assert updated_goal["status"] == "in progress"
    assert updated_goal["priority"] == "high"
    assert updated_goal["due_date"] == "2025-12-31T23:59:59"

    # Verify the goal was updated in the database
    with next(get_session()) as session:
        goal_in_db = session.get(Goal, goal.id)
        assert goal_in_db is not None
        assert goal_in_db.name == "Updated Goal"
        assert goal_in_db.description == "An updated goal"
        assert goal_in_db.status == "in progress"
        assert goal_in_db.priority == "high"
        assert goal_in_db.due_date.isoformat() == "2025-12-31T23:59:59"

def test_update_non_existing_goal(client: TestClient) -> None:
    """Test the update_goal endpoint with a non-existing goal.

    This test checks if the update_goal endpoint returns a 404 status code
    when the goal does not exist.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    goal_data = {
        "name": "Updated Goal"
    }
    # Make a request to the delete_goal endpoint with a non-existing goal ID
    response = client.put("/v1/goals/999", json=goal_data)

    # Check the response
    assert response.status_code == 404

def test_update_goal_without_optional_fields(client: TestClient) -> None:
    """Test the update_goal endpoint without optional fields.

    This test checks if the update_goal endpoint correctly updates an existing goal
    when only the required fields are provided.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Initialize a test goal
    goal = initialize_goal()

    updated_goal_data = {
        "name": "Updated Goal"
    }

    # Make a request to the update_goal endpoint
    response = client.put(f"/v1/goals/{goal.id}", json=updated_goal_data)

    # Check the response
    assert response.status_code == 200
    updated_goal = response.json()
    assert updated_goal["name"] == "Updated Goal"
    assert updated_goal["description"]is None
    assert updated_goal["status"] == "to refine"
    assert updated_goal["priority"] == "medium"
    assert updated_goal["due_date"] is None

def test_update_goal_without_fields(client: TestClient) -> None:
    """Test the update_goal endpoint without fields.

    This test checks if the update_goal endpoint returns a 422 status code
    when all fields are missing.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Initialize a test goal
    goal = initialize_goal()

    updated_goal_data = {}

    # Make a request to the update_goal endpoint
    response = client.put(f"/v1/goals/{goal.id}", json=updated_goal_data)

    # Check the response
    assert response.status_code == 422

def test_update_goal_empty_name(client: TestClient) -> None:
    """Test the update_goal endpoint with an empty name.

    This test checks if the update_goal endpoint returns a 422 status code
    when the name field is empty.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Initialize a test goal
    goal = initialize_goal()

    updated_goal_data = {
        "name": ""
    }

    # Make a request to the update_goal endpoint
    response = client.put(f"/v1/goals/{goal.id}", json=updated_goal_data)

    # Check the response
    assert response.status_code == 422

def test_update_goal_with_none_name(client: TestClient) -> None:
    """Test the update_goal endpoint with None name.

    This test checks if the update_goal endpoint returns a 422 status code
    when the name field is None.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Initialize a test goal
    goal = initialize_goal()

    updated_goal_data = {
        "name": None
    }

    # Make a request to the update_goal endpoint
    response = client.put(f"/v1/goals/{goal.id}", json=updated_goal_data)

    # Check the response
    assert response.status_code == 422

def test_update_goal_with_empty_description(client: TestClient) -> None:
    """Test the update_goal endpoint with an empty description.

    This test checks if the update_goal endpoint correctly updates an existing goal
    when the description field is empty.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Initialize a test goal
    goal = initialize_goal()

    updated_goal_data = {
        "name": "Updated Goal",
        "description": ""
    }

    # Make a request to the update_goal endpoint
    response = client.put(f"/v1/goals/{goal.id}", json=updated_goal_data)

    # Check the response
    assert response.status_code == 200
    updated_goal = response.json()
    assert updated_goal["name"] == "Updated Goal"
    assert updated_goal["description"] == ""
    assert updated_goal["status"] == "to refine"
    assert updated_goal["priority"] == "medium"
    assert updated_goal["due_date"] is None

def test_update_goal_with_none_description(client: TestClient) -> None:
    """Test the update_goal endpoint with a None description.

    This test checks if the update_goal endpoint correctly updates an existing goal
    when the description field is None.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Initialize a test goal
    goal = initialize_goal()

    updated_goal_data = {
        "name": "Updated Goal",
        "description": None
    }

    # Make a request to the update_goal endpoint
    response = client.put(f"/v1/goals/{goal.id}", json=updated_goal_data)

    # Check the response
    assert response.status_code == 200
    updated_goal = response.json()
    assert updated_goal["name"] == "Updated Goal"
    assert updated_goal["description"] is None
    assert updated_goal["status"] == "to refine"
    assert updated_goal["priority"] == "medium"
    assert updated_goal["due_date"] is None

def test_update_goal_with_empty_status(client: TestClient) -> None:
    """Test the update_goal endpoint with an empty status.

    This test checks if the update_goal endpoint returns a 422 status code
    when the status field is empty.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Initialize a test goal
    goal = initialize_goal()

    updated_goal_data = {
        "name": "Updated Goal",
        "status": ""
    }

    # Make a request to the update_goal endpoint
    response = client.put(f"/v1/goals/{goal.id}", json=updated_goal_data)

    # Check the response
    assert response.status_code == 422

def test_update_goal_with_none_status(client: TestClient) -> None:
    """Test the update_goal endpoint with a None status.

    This test checks if the update_goal endpoint correctly updates an existing goal
    when the status field is None.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Initialize a test goal
    goal = initialize_goal()

    updated_goal_data = {
        "name": "Updated Goal",
        "status": None
    }

    # Make a request to the update_goal endpoint
    response = client.put(f"/v1/goals/{goal.id}", json=updated_goal_data)

    # Check the response
    assert response.status_code == 200
    updated_goal = response.json()
    assert updated_goal["name"] == "Updated Goal"
    assert updated_goal["description"] is None
    assert updated_goal["status"] == "to refine"
    assert updated_goal["priority"] == "medium"
    assert updated_goal["due_date"] is None

def test_update_goal_with_bad_status(client: TestClient) -> None:
    """Tests the update_goal endpoint with bad status.

    This test checks if the update_goal endpoint returns a 422 status code
    when the status field has a bad value.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Initialize a test goal
    goal = initialize_goal()

    updated_goal_data = {
        "name": "Updated Goal",
        "status": "bad status"
    }

    # Make a request to the update_goal endpoint
    response = client.put(f"/v1/goals/{goal.id}", json=updated_goal_data)

    # Check the response
    assert response.status_code == 422

def test_update_goal_with_empty_priority(client: TestClient) -> None:
    """Test the update_goal endpoint with an empty priority.

    This test checks if the update_goal endpoint returns a 422 status code
    when the priority field is empty.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Initialize a test goal
    goal = initialize_goal()

    updated_goal_data = {
        "name": "Updated Goal",
        "priority": ""
    }

    # Make a request to the update_goal endpoint
    response = client.put(f"/v1/goals/{goal.id}", json=updated_goal_data)

    # Check the response
    assert response.status_code == 422

def test_update_goal_with_none_priority(client: TestClient) -> None:
    """Test the update_goal endpoint with a None priority.

    This test checks if the update_goal endpoint correctly updates an existing goal
    when the priority field is None.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Initialize a test goal
    goal = initialize_goal()

    updated_goal_data = {
        "name": "Updated Goal",
        "priority": None
    }

    # Make a request to the update_goal endpoint
    response = client.put(f"/v1/goals/{goal.id}", json=updated_goal_data)

    # Check the response
    assert response.status_code == 200
    updated_goal = response.json()
    assert updated_goal["name"] == "Updated Goal"
    assert updated_goal["description"] is None
    assert updated_goal["status"] == "to refine"
    assert updated_goal["priority"] == "medium"
    assert updated_goal["due_date"] is None

def test_update_goal_with_bad_priority(client: TestClient) -> None:
    """Tests the update_goal endpoint with bad priority.

    This test checks if the update_goal endpoint returns a 422 status code
    when the priority field has a bad value.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Initialize a test goal
    goal = initialize_goal()

    updated_goal_data = {
        "name": "Updated Goal",
        "priority": "bad priority"
    }

    # Make a request to the update_goal endpoint
    response = client.put(f"/v1/goals/{goal.id}", json=updated_goal_data)

    # Check the response
    assert response.status_code == 422

def test_update_goal_with_empty_due_date(client: TestClient) -> None:
    """Test the update_goal endpoint with an empty due date.

    This test checks if the update_goal endpoint returns a 422 status code
    when the due_date field is empty.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Initialize a test goal
    goal = initialize_goal()

    updated_goal_data = {
        "name": "Updated Goal",
        "due_date": ""
    }

    # Make a request to the update_goal endpoint
    response = client.put(f"/v1/goals/{goal.id}", json=updated_goal_data)

    # Check the response
    assert response.status_code == 422

def test_update_goal_with_none_due_date(client: TestClient) -> None:
    """Test the update_goal endpoint with a None due date.

    This test checks if the update_goal endpoint correctly updates an existing goal
    when the due_date field is None.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Initialize a test goal
    goal = initialize_goal()

    updated_goal_data = {
        "name": "Updated Goal",
        "due_date": None
    }

    # Make a request to the update_goal endpoint
    response = client.put(f"/v1/goals/{goal.id}", json=updated_goal_data)

    # Check the response
    assert response.status_code == 200
    updated_goal = response.json()
    assert updated_goal["name"] == "Updated Goal"
    assert updated_goal["description"] is None
    assert updated_goal["status"] == "to refine"
    assert updated_goal["priority"] == "medium"
    assert updated_goal["due_date"] is None

def test_delete_existing_goal(client: TestClient) -> None:
    """Test the delete_goal endpoint with an existing goal.

    This test checks if the delete_goal endpoint correctly deletes an existing goal.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Initialize a test goal
    goal = initialize_goal()

    # Make a request to the delete_goal endpoint
    response = client.delete(f"/v1/goals/{goal.id}")

    # Check the response
    assert response.status_code == 204

    # Verify the goal was deleted from the database
    with next(get_session()) as session:
        goal_in_db = session.get(Goal, goal.id)
        assert goal_in_db is None

def test_delete_non_existing_goal(client: TestClient) -> None:
    """Test the delete_goal endpoint with a non-existing goal.

    This test checks if the delete_goal endpoint returns a 404 status code
    when the goal does not exist.

    Args:
        client (TestClient): The test client for making requests to the FastAPI app.
    """
    # Make a request to the delete_goal endpoint with a non-existing goal ID
    response = client.delete("/v1/goals/999")

    # Check the response
    assert response.status_code == 404
    assert response.json() == {"detail": "Goal not found"}
