from datetime import datetime
from typing import Literal, Optional, List

from pydantic import BaseModel, Field


class TaskResponse(BaseModel):
    id: str = Field(
        ...,
        description="Unique identifier of the task"
    )
    title: str = Field(
        ...,
        description="Title of the task"
    )
    status: Literal["active", "complete"] = Field(
        default="active",
        description="Current status of the task"
    )
    completed_at: Optional[datetime] = Field(
        default=None,
        description="Timestamp when the task was completed, if applicable"
    )
    created_at: datetime = Field(
        ...,
        description="Timestamp when the task was created"
    )
    updated_at: datetime = Field(
        ...,
        description="Timestamp when the task was last updated"
    )
    

class TasksResponse(BaseModel):
    tasks: List[TaskResponse] = Field(
        ...,
        description="List of tasks"
    )
    complete_count: int = Field(
        ...,
        description="Number of completed tasks"
    )
    active_count: int = Field(
        ...,
        description="Number of active tasks"
    )
    

class CreateTaskRequest(BaseModel):
    title: str = Field(
        ..., 
        description="Title of the task"
    )


class UpdateTaskRequest(BaseModel):
    title: Optional[str] = Field(
        default=None,
        description="New title for the task"
    )
    status: Optional[Literal["active", "complete"]] = Field(
        default=None,
        description="Updated task status"
    )
    completed_at: Optional[datetime] = Field(
        default=None,
        description="Timestamp when the task was completed"
    )