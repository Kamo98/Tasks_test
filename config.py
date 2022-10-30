from starlette.config import Config

config = Config(".env")

# URL для подключения к БД
DATABASE_URL = config("DATABASE_URL", cast=str, default="")
