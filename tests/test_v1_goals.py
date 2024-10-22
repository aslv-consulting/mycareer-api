"""
test_v1_goals.py

This module contains tests for the API endpoints defined in v1_goals.py.

Fixtures:
    client_fixture: Creates a TestClient for the FastAPI app.

Functions:
    initialize_goal: Initializes a test goal in the database.
    test_get_goals: Tests the get_goals endpoint.
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
