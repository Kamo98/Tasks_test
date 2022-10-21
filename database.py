from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DATABASE_URL

# Подключение к БД
engine = create_engine(DATABASE_URL, echo=True)
# Получение базовой ORM сущности
Base = declarative_base()
# Создание сессии
Session = sessionmaker(bind=engine)


