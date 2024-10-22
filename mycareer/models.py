"""
models.py

This module defines the data models for the My Career API using SQLModel.

Classes:
    GoalStatus: An enumeration representing the possible statuses of a goal.
    GoalPriority: An enumeration representing the possible priorities of a goal.
    Goal: A model representing a goal with attributes such as id, name, description, 
    status, priority, and due date.
"""

from datetime import datetime
from enum import Enum
from sqlmodel import Field, SQLModel

class GoalStatus(str, Enum):
    """
    ## Description

    An enumeration representing the possible statuses of a goal.

    ## Attributes

        TO_REFINE (str): The goal needs to be refined.

        NOT_STARTED (str): The goal has not been started.

        IN_PROGRESS (str): The goal is currently in progress.

        BLOCKED (str): The goal is blocked.
    
        COMPLETED (str): The goal has been completed.
        
        ABANDONED (str): The goal has been abandoned.
    """
    TO_REFINE = "to refine"
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    BLOCKED = "blocked"
    COMPLETED = "completed"
    ABANDONED = "abandoned"

class GoalPriority(str, Enum):
    """
    ## Description

    An enumeration representing the possible priorities of a goal.

    ## Attributes

        LOW (str): The goal has low priority.
    
        MEDIUM (str): The goal has medium priority.
    
        HIGH (str): The goal has high priority.
    """
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Goal(SQLModel, table=True):
    """
    ## Description
    
    A model representing a goal.

    ## Attributes
        
        id (int | None): The unique identifier for the goal. Defaults to None.
        
        name (str): The name of the goal.
        
        description (str | None): A description of the goal. Defaults to None.
        
        status (GoalStatus): The status of the goal. Defaults to GoalStatus.TO_REFINE.
        
        priority (GoalPriority): The priority of the goal. Defaults to GoalPriority.MEDIUM.
        
        due_date (datetime | None): The due date of the goal. Defaults to None.
    """
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str | None = Field(default=None)
    status: GoalStatus = Field(default=GoalStatus.TO_REFINE, index=True)
    priority: GoalPriority = Field(default=GoalPriority.MEDIUM, index=True)
    due_date: datetime | None = Field(default=None, index=True)
