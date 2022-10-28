from pydantic import BaseModel, UUID4

# Модели задачи для клиента


class TaskParams (BaseModel):
    param_1: str
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
    description: str
    params: TaskParams

    class Config:
        orm_mode = True
