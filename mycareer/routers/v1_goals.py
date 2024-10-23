"""
This module defines the API endpoints for managing goals in the My Career API.

Functions:
    get_goals: Endpoint to get all goals.
    create_goal: Endpoint to create a new goal.
    get_goal: Endpoint to get a single goal by ID.
    delete_goal: Endpoint to delete a goal by ID.
"""

from typing import Annotated, List
from fastapi import Depends, APIRouter, HTTPException
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

@router.get("/{goal_id}", response_model=GoalRead, tags=["goals"])
async def get_goal(goal_id: int, session: SessionDep) -> GoalRead:
    """
    ## Description

    Endpoint to get a single goal by ID.

    ## Args

        goal_id (int): The ID of the goal to be retrieved.

    ## Returns

        GoalRead: The goal object.

    ## Raises

        HTTPException: If the goal with the given ID does not exist.
    """
    goal = session.get(Goal, goal_id)
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal

@router.delete("/{goal_id}", status_code=204, tags=["goals"])
async def delete_goal(goal_id: int, session: SessionDep) -> None:
    """
    ## Description

    Endpoint to delete a goal.

    ## Args

        goal_id (int): The ID of the goal to be deleted.

    ## Raises

        HTTPException: If the goal with the given ID does not exist.
    """
    goal = session.get(Goal, goal_id)
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    session.delete(goal)
    session.commit()
