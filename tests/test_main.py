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

def test_echo() -> None:
    """Test the echo endpoint.

    This test checks if the echo endpoint ("/") returns a status code of 200
    and the expected JSON response.

    Asserts:
        response.status_code: The HTTP status code of the response.
        response.json(): The JSON body of the response.
    """
    response = client.get("/echo")
    assert response.status_code == 200
    assert response.json() == {"message": "echo"}
