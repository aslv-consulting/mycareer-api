"""
This module contains tests for the FastAPI application defined in mycareer.main.

The tests use the FastAPI TestClient to make requests to the application and
verify the responses.

Functions:
    test_root: Tests the root endpoint ("/").
"""

from fastapi.testclient import TestClient
from mycareer.main import app

client = TestClient(app)

def test_root() -> None:
    """Test the root endpoint.

    This test checks if the root endpoint ("/") returns a status code of 200
    and the expected JSON response.

    Asserts:
        response.status_code: The HTTP status code of the response.
        response.json(): The JSON body of the response.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
