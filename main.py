import uvicorn
from fastapi import FastAPI, status
from endpoints.task_endpoint import router

app = FastAPI()
app.include_router(router)


# Для удобства тестирования и отладки
if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
