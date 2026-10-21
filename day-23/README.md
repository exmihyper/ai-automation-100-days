# День 23: REST API для AI-сервисов ✅

**Дата:** 21 октября 2026

## Что сделано
- [x] Установлен `httpx`, `python-dotenv`, `pydantic-settings`
- [x] Создан `.env` с токенами (chmod 600, не в git)
- [x] Создан `config.py` с Pydantic Settings
- [x] Обновлён `main.py` — добавлен `POST /chat`
- [x] Интеграция с Cloudflare Workers AI через httpx
- [x] Pydantic-модели для валидации (`ChatRequest`, `ChatResponse`)
- [x] Обработка ошибок (`HTTPException`)
- [x] Тест через `/docs` — ответ 200

## Структура
/root/fastapi-app/
├── venv/
├── .env # токены (не в git)
├── config.py # Pydantic Settings
└── main.py # FastAPI + /chat


## Эндпоинты
| Метод | Путь | Что делает |
|-------|------|------------|
| GET | `/` | Приветствие |
| GET | `/health` | Healthcheck |
| POST | `/chat` | AI-ответ через Cloudflare |

## Пример запроса
```bash
curl -X POST "http://46.17.102.81:8001/chat" \
  -H "Content-Type: application/json" \
  -d '{"message":"Что такое FastAPI?"}'