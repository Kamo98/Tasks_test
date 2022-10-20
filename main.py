import uuid
from typing import List

import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel, UUID4

app = FastAPI()


class TaskParams (BaseModel):
    param_1: str
    param_2: int


class Task (BaseModel):
    description: str
    params: TaskParams


@app.post(
    "/tasks/add",
    response_model=Task,
    status_code=status.HTTP_200_OK
)
async def create_task(task: Task):
    return task


@app.get(
    "/tasks",
    response_model=List[Task],
    status_code=status.HTTP_200_OK
)
async def read_tasks():
    return []


@app.put(
    "/tasks/{task_id}",
    response_model=Task,
    status_code=status.HTTP_200_OK
)
async def update_task(task_id: UUID4, task: Task):
    return task


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
