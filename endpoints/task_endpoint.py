from fastapi import APIRouter, status
from repositories.task_repo import TaskRepository
from services.task_service import TaskService
from schemas.task_schema import Task as SchemaTask
from typing import List
from pydantic import UUID4

router = APIRouter()
task_service = TaskService(TaskRepository())


@router.post(
    "/tasks/add",
    status_code=status.HTTP_201_CREATED
)
async def create_task(task: SchemaTask):
    task_service.create(task)


@router.get(
    "/tasks",
    response_model=List[SchemaTask],
    status_code=status.HTTP_200_OK
)
async def get_all_tasks() -> List[SchemaTask]:
    return task_service.get_all()


@router.put(
    "/tasks/{task_id}",
    status_code=status.HTTP_200_OK
)
async def update_task(task_id: UUID4, task: SchemaTask):
    task_service.update(task_id, task)
