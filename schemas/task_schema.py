from pydantic import BaseModel, UUID4, Field


# Модели задачи для клиента


class TaskParams (BaseModel):
    param_1: str = Field(max_length=10)
    param_2: int

    class Config:
        orm_mode = True


class TaskOut (BaseModel):
    task_uuid: UUID4
    description: str
    params: TaskParams

    class Config:
        orm_mode = True


class TaskIn (BaseModel):
    description: str = Field(max_length=20)
    params: TaskParams

    class Config:
        orm_mode = True
