import os
import random

from fastapi import FastAPI
from dotenv import load_dotenv


app = FastAPI(title="Монетка")
load_dotenv()

@app.get("/")
def root():
    return {"message": "Подбросьте монетку"}

@app.get("/quantity")
async def quantity(qu: int = 1):
    app.state.qu = qu
    return {"Количество монет": qu}

@app.on_event("startup")
async def startup():
    app.state.qu = 1
    app.state.count = 0
    app.state.count_heads = 0
    app.state.count_tails = 0

@app.get("/reset")
async def reset():
    app.state.qu = 1
    app.state.count = 0
    app.state.count_heads = 0
    app.state.count_tails = 0
    return ('Статистика сброшена')

@app.get("/throw")
async def throw():
    d = []
    for i in range(app.state.qu):
        app.state.count += 1
        if random.randint(0, 1) == 1:
            app.state.count_heads += 1
            d.append("ОРЕЛ")
        else:
            app.state.count_tails += 1
            d.append("РЕШКА")
    return d

@app.get("/stats")
async def stats():
    return {
	"Всего бросков": app.state.count,
        "Орел": app.state.count_heads,
        "Решка": app.state.count_tails,
    }

@app.get("/version")
def version():
    return {"version":"0.1.1"}

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/info")
def info():
    app_name = os.getenv("APP_NAME", "Монетка")
    app_author = os.getenv("APP_AUTHOR", "Не указан")

    return {
        "app_name": app_name,
        "author": app_author,
    }
