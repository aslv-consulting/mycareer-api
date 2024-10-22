"""
test_database.py

This module contains tests for the database connection and session management
defined in mycareer.database.

Functions:
    test_get_session: Tests the get_session function.
"""

from sqlmodel import Session
from mycareer.database import get_session

def test_get_session() -> None:
    """Test the get_session function.

    This test checks if the get_session function yields a valid database session.

    Asserts:
        session: The yielded session should be an instance of sqlmodel.Session.
    """
    session_generator = get_session()
    session = next(session_generator)
    assert isinstance(session, Session)
    session.close()
