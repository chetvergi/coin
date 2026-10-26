# Приложение МОНЕТКА

Приложение имитирует бросок монетки и определяет результат броска и сохраняет статистику бросков в текущей сессии.


## Установка

###  1. Клонирование репозитория

```bash
git clone https://github.com/chetvergi/coin.git
cd coin
```

###  2. Создание виртуального окружения

```bash
python3 -m venv .venv
source .venv/bin/activate
```

###  3. Установка зависимостей

```bash
python -m pip install -r requirements.txt
python -m pip install -r requirements_dev.txt
```

## Запуск

```bash
python -m uvicorn app:app --reload
```

После запуска:

- приложение: http://127.0.0.1:8000
- документация: http://127.0.0.1:8000/docs



## Запуск тестов

```bash
python -m pytest -v
```
