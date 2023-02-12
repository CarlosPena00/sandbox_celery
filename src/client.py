from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.main import slow_fibonacci

app = FastAPI(swagger_ui_parameters={"displayRequestDuration": True})


@app.get("/")
def to_docs():
    return RedirectResponse("/docs")


@app.get("/fibonacci")
async def fibonacci(n: int = 10):
    result = slow_fibonacci.delay(n).get()
    return result
