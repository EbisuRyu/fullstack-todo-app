from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from mongoengine import DoesNotExist, ValidationError

from src.services import TaskService
from src.schemas import (
    CreateTaskRequest,
    UpdateTaskRequest,
    TaskResponse,
    TasksResponse
)
from src.dependencies import get_task_service


router = APIRouter()


@router.get("/", response_model=TasksResponse, summary="Get all tasks")
def get_tasks(
    filter: str = "today",
    task_service: TaskService = Depends(get_task_service)
):
    try:
        result = task_service.get_all_tasks(filter=filter)
        return TasksResponse.model_validate(result)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to fetch tasks: {e}"
        )


@router.get("/{task_id}", response_model=TaskResponse, summary="Get task by ID")
def get_task_by_id(task_id: str, task_service: TaskService = Depends(get_task_service)):
    try:
        task_data = task_service.get_task_by_id(task_id)
        return TaskResponse.model_validate(task_data)
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error: {e}"
        )


@router.post("/", status_code=status.HTTP_201_CREATED, summary="Create task")
def create_task(payload: CreateTaskRequest, task_service: TaskService = Depends(get_task_service)):
    try:
        task_service.create_task(data=payload.model_dump())
        return {"message": "Task created successfully"}
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Validation error: {e}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to create task: {e}"
        )


@router.put("/{task_id}", summary="Update task")
def update_task(
    task_id: str,
    payload: UpdateTaskRequest,
    task_service: TaskService = Depends(get_task_service)
):
    try:
        task_service.update_task(task_id, payload.model_dump(exclude_none=True))
        return {"message": "Task updated successfully"}
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to update task: {e}"
        )


@router.delete("/{task_id}", summary="Delete task")
def delete_task(task_id: str, task_service: TaskService = Depends(get_task_service)):
    try:
        task_service.delete_task(task_id)
        return {"message": "Task deleted successfully"}
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to delete task: {e}"
        )