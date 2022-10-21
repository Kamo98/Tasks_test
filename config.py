from starlette.config import Config

config = Config(".env_dev")

# URL для подключения к БД
DATABASE_URL = config("DATABASE_URL", cast=str, default="")
