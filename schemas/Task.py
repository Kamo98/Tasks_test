from pydantic import BaseModel
from models.Task import Task as ModelTask


# Модель задачи для клиента

class TaskParams (BaseModel):
    param_1: str
    param_2: int

    class Config:
        orm_mode = True


class Task (BaseModel):
    description: str
    params: TaskParams

    # def __init__(self, task: ModelTask, *args, **kwargs):
    #     self.description = task.description
    #     self.params = TaskParams(
    #         param_1=task.param_1,
    #         param_2=task.param_2
    #     )


    class Config:
        orm_mode = True
