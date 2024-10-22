"""
This module defines the API endpoints for managing goals in the My Career API.

Functions:
    get_goals: Endpoint to get all goals.
"""

from typing import Annotated, List
from fastapi import Depends, APIRouter
from sqlmodel import Session, select
from mycareer.database import get_session
from mycareer.models import Goal

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(
    prefix="/v1/goals",
    tags=["goals"]
)

@router.get("", response_model=List[Goal], tags=["goals"])
async def get_goals(session: SessionDep) -> List[Goal]:
    """
    ## Description

    Endpoint to get all goals.

    ## Returns
        
        List[Goal]: A list containing all goals.
    """
    goals = session.exec(select(Goal)).all()
    return goals
