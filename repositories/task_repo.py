from typing import List

from database import SessionDB
from models.task_model import Task as ModelTask
import uuid


class TaskRepository:
    def __init__(self):
        self.db = SessionDB()

    # Создание новой задачи
    def create(self, task: ModelTask) -> ModelTask:
        self.db.add(task)
        self.db.commit()
        return task

    # Получение всех задач
    def get_all(self) -> List[ModelTask]:
        return self.db.query(ModelTask).all()

    # Обновление задачи
    def update(self, task_id: uuid, description: str, param_1: str, param_2: int) -> ModelTask:
        task: ModelTask = self.db.query(ModelTask).filter(ModelTask.task_uuid == task_id).first()

        # Если задача не найдена
        if task is None:
            #todo: выбрасывать исключение
            return None

        # Обновление полей
        task.description = description
        task.param_1 = param_1
        task.param_2 = param_2

        self.db.commit()
        return task
