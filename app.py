import os
import random

from fastapi import FastAPI
from dotenv import load_dotenv


app = FastAPI(title="Монетка")
load_dotenv()

@app.get("/")
def root():
    return {"message": "Подбросьте монетку"}

@app.on_event("startup")
async def startup():
    app.state.count = 0
    app.state.count_heads = 0
    app.state.count_tails = 0

@app.get("/throw")
async def throw():
    app.state.count += 1
    if random.randint(0, 1) == 1:
        app.state.count_heads += 1
        return {"result": "ОРЁЛ"}
    else:
        app.state.count_tails += 1
        return {"result": "РЕШКА"}


@app.get("/stats")
async def stats():
    return {
	"Всего бросков": app.state.count,
        "Орел": app.state.count_heads,
        "Решка": app.state.count_tails,
    }

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/info")
def info():
    app_name = os.getenv("APP_NAME", "Учебный сервис")
    app_author = os.getenv("APP_AUTHOR", "Не указан")

    return {
        "app_name": app_name,
        "author": app_author,
    }
