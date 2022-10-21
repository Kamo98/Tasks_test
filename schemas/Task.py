from pydantic import BaseModel


# Модель задачи для клиента

class TaskParams (BaseModel):
    param_1: str
    param_2: int

    class Config:
        orm_mode = True


class Task (BaseModel):
    description: str
    params: TaskParams

    class Config:
        orm_mode = True
