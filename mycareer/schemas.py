"""
This module defines the Pydantic schemas for the My Career API.
"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, model_validator
from typing_extensions import Annotated
from mycareer.models import GoalStatus, GoalPriority

class GoalBase(BaseModel):
    """
    Base schema for a goal.

    ## Attributes
        
        name (Annotated[str, Field(..., min_length=1)]): The name of the goal.
        
        description (Optional[str]): A description of the goal.
        
        status (GoalStatus): The status of the goal.
        
        priority (GoalPriority): The priority of the goal.
        
        due_date (Optional[datetime]): The due date of the goal.
    """
    name: Annotated[str, Field(..., min_length=1)]
    description: Optional[str] = None
    status: GoalStatus = GoalStatus.TO_REFINE
    priority: GoalPriority = GoalPriority.MEDIUM
    due_date: Optional[datetime] = None

class GoalCreate(GoalBase):
    """
    ## Description

    Schema for creating a goal.

    ## Attributes
        
        name (Annotated[str, Field(..., min_length=1)]): The name of the goal.
        
        description (Optional[str]): A description of the goal.
        
        status (Optional[GoalStatus]): The status of the goal.
        
        priority (Optional[GoalPriority]): The priority of the goal.
        
        due_date (Optional[datetime]): The due date of the goal.
    """
    description: Optional[str] = None
    status: Optional[GoalStatus] = GoalStatus.TO_REFINE
    priority: Optional[GoalPriority] = GoalPriority.MEDIUM
    due_date: Optional[datetime] = None

    @model_validator(mode='before')
    @classmethod
    def set_defaults(cls, values):
        """Set default values for status and priority if they are None."""
        if values.get('status') is None:
            values['status'] = GoalStatus.TO_REFINE
        if values.get('priority') is None:
            values['priority'] = GoalPriority.MEDIUM
        return values

class GoalRead(GoalBase):
    """
    ## Description

    Schema for reading a goal.

    ## Attributes

        id (int): The unique identifier for the goal.

        name (Annotated[str, Field(..., min_length=1)]): The name of the goal.
        
        description (Optional[str]): A description of the goal.
        
        status (GoalStatus): The status of the goal.
        
        priority (GoalPriority): The priority of the goal.
        
        due_date (Optional[datetime]): The due date of the goal.
    """
    id: int

    class Config:
        """Pydantic configuration for GoalRead."""
        orm_mode = True

class GoalUpdate(BaseModel):
    """
    ## Description

    Schema for updating a goal.

    ## Attributes
        
        name (Optional[Annotated[str, Field(..., min_length=1)]]): The name of the goal.
        
        description (Optional[str]): A description of the goal.
        
        status (Optional[GoalStatus]): The status of the goal.
        
        priority (Optional[GoalPriority]): The priority of the goal.
        
        due_date (Optional[datetime]): The due date of the goal.
    """
    name: Optional[Annotated[str, Field(..., min_length=1)]] = None
    description: Optional[str] = None
    status: Optional[GoalStatus] = None
    priority: Optional[GoalPriority] = None
    due_date: Optional[datetime] = None
