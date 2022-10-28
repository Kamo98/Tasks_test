from pydantic import BaseModel, UUID4


# Модель задачи для клиента

class TaskParams (BaseModel):
    param_1: str
    param_2: int

    class Config:
        orm_mode = True


class Task (BaseModel):
    task_uuid: UUID4    #todo: сделать необязательным
    description: str
    params: TaskParams

    class Config:
        orm_mode = True
