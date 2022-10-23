import uuid
from typing import List

import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel, UUID4
from schemas.Task import Task as SchemaTask, TaskParams
from models.Task import Task as ModelTask
from repositories.TaskRepository import TaskRepository

app = FastAPI()
task_repo = TaskRepository()


@app.post(
    "/tasks/add",
    status_code=status.HTTP_201_CREATED
)
async def create_task(task: SchemaTask):
    new_task = ModelTask(
        description=task.description,
        param_1=task.params.param_1,
        param_2=task.params.param_2
    )
    task_repo.create(new_task)


@app.get(
    "/tasks",
    response_model=List[SchemaTask],
    status_code=status.HTTP_200_OK
)
async def get_all_tasks() -> List[SchemaTask]:
    tasks = task_repo.get_all()
    schema_tasks = [SchemaTask(
        description=t.description,
        params=TaskParams(
            param_1=t.param_1,
            param_2=t.param_2
        )
    ) for t in tasks]
    return schema_tasks


@app.put(
    "/tasks/{task_id}",
    status_code=status.HTTP_200_OK
)
async def update_task(task_id: UUID4, task: SchemaTask):
    task_repo.update(
        task_id,
        description=task.description,
        param_1=task.params.param_1,
        param_2=task.params.param_2
    )


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
