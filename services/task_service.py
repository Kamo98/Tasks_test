import uuid

from repositories.task_repo import TaskRepository
from schemas.task_schema import Task as SchemaTask, TaskParams
from models.task_model import Task as ModelTask


class TaskService:

    def __init__(self, task_repo: TaskRepository):
        self.repo: TaskRepository = task_repo

    # Создание новой задачи
    def create(self, task: SchemaTask):
        new_task = ModelTask(
            description=task.description,
            param_1=task.params.param_1,
            param_2=task.params.param_2
        )
        self.repo.create(new_task)

    # Получение всех задач
    def get_all(self):
        tasks = self.repo.get_all()
        schema_tasks = [SchemaTask(
            task_uuid=t.task_uuid,
            description=t.description,
            params=TaskParams(
                param_1=t.param_1,
                param_2=t.param_2
            )
        ) for t in tasks]
        return schema_tasks

    # Обновление задачи
    def update(self, task_id: uuid, task: SchemaTask):
        self.repo.update(
            task_id,
            description=task.description,
            param_1=task.params.param_1,
            param_2=task.params.param_2
        )

