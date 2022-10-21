from database import Base, engine
from models import Task

# Генерация структуры БД
Base.metadata.create_all(bind=engine)
