from database import Base
from sqlalchemy import Integer, String, Column
from sqlalchemy.dialects.postgresql import UUID
import uuid


# Модель задачи
class Task(Base):
    __tablename__ = "task"

    task_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    description = Column(String(255))
    param_1 = Column(String(50))
    param_2 = Column(Integer)
