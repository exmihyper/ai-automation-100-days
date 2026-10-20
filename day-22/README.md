# День 22: Python + FastAPI — основы ✅

**Дата:** 20 октября 2026

## Что сделано
- [x] Установлен Python 3.12 + pip + venv на сервер
- [x] Создано виртуальное окружение `/root/fastapi-app/venv`
- [x] Установлен FastAPI + Uvicorn
- [x] Создан `main.py` с 3 эндпоинтами:
  - `GET /` — приветствие
  - `GET /health` — healthcheck
  - `GET /items/{item_id}` — параметры запроса
- [x] Сервер запущен на порту 8001
- [x] Swagger UI работает на `/docs`
- [x] Проверены все эндпоинты через браузер

## Структура

/root/fastapi-app/
├── venv/ # виртуальное окружение
└── main.py # FastAPI приложение



cd /root/fastapi-app
source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8001