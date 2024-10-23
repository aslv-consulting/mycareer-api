"""
This module defines the API endpoints for managing goals in the My Career API.

Functions:
    get_goals: Endpoint to get all goals.
    create_goal: Endpoint to create a new goal.
"""

from typing import Annotated, List
from fastapi import Depends, APIRouter
from sqlmodel import Session, select
from mycareer.database import get_session
from mycareer.models import Goal
from mycareer.schemas import GoalCreate, GoalRead

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(
    prefix="/v1/goals",
    tags=["goals"]
)

@router.get("", response_model=List[GoalRead], tags=["goals"])
async def get_goals(session: SessionDep) -> List[GoalRead]:
    """
    ## Description

    Endpoint to get all goals.

    ## Returns
        
        List[GoalRead]: A list containing all goals.
    """
    goals = session.exec(select(Goal)).all()
    return goals

@router.post("", response_model=GoalRead, tags=["goals"])
async def create_goal(goal: GoalCreate, session: SessionDep) -> GoalRead:
    """
    ## Description

    Endpoint to create a new goal.

    ## Args

        goal (GoalCreate): The goal object to be created.

    ## Returns

        GoalRead: The created goal object.
    """
    db_goal = Goal.from_orm(goal)
    session.add(db_goal)
    session.commit()
    session.refresh(db_goal)
    return db_goal
