import os
import random

from fastapi import FastAPI
from dotenv import load_dotenv


app = FastAPI(title="Монетка")
load_dotenv()

@app.get("/")
def root():
    return {"message": "Подбросьте монетку"}

count = 0
count_heads = 0
count_tails = 0

@app.get("/throw")
def throw():
    count += 1
    if random.randint(0, 1) == 1:
	count_heads += 1
        return {"result": "ОРЁЛ"}
    else:
        return {"result": "РЕШКА"}
	count_tails += 1

@app.get("/stats")
def stats()
    return {
	"Всего бросков": count
	"Орел": count_heads
	"Решка": count_tails
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
