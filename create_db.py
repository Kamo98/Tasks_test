from database import Base, engine
from models import task_model

# Генерация структуры БД
Base.metadata.create_all(bind=engine)