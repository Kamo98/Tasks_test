import uvicorn
from fastapi import FastAPI, status
from endpoints.task_endpoint import router
from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions import TaskNotFoundException

app = FastAPI()
app.include_router(router)


@app.exception_handler(TaskNotFoundException)
def task_not_found_exception_handler(request: Request, exception: TaskNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": exception.msg}
    )


if __name__ == "__main__":
    # Для удобства тестирования и отладки
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
