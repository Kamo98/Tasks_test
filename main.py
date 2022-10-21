import uuid
from typing import List

import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel, UUID4
from schemas import Task as SchemaTask

app = FastAPI()


@app.post(
    "/tasks/add",
    response_model=SchemaTask,
    status_code=status.HTTP_201_CREATED
)
async def create_task(task: SchemaTask):
    return task


@app.get(
    "/tasks",
    response_model=List[SchemaTask],
    status_code=status.HTTP_200_OK
)
async def read_tasks():
    return []


@app.put(
    "/tasks/{task_id}",
    response_model=SchemaTask,
    status_code=status.HTTP_200_OK
)
async def update_task(task_id: UUID4, task: SchemaTask):
    return task


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
