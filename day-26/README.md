# День 26: Интеграция FastAPI + n8n ✅

**Дата:** 4 ноября 2026

## Что сделано
- [x] Добавлен **OpenAI-совместимый эндпоинт** `/v1/chat/completions` в FastAPI
- [x] Добавлен **`/v1/models`** для Credential в n8n
- [x] Создан Credential **OpenAI** с Base URL `http://46.17.102.81:8001/v1`
- [x] Заменён **Cloudflare Chat Model** на **OpenAI Chat Model** (FastAPI)
- [x] `Use Responses API` выключен (FastAPI не поддерживает `/v1/responses`)
- [x] Вся цепочка работает: n8n → FastAPI → Cloudflare → ответ

## Архитектура
[Telegram] → [n8n] → [FastAPI] → [Cloudflare] → ответ → Telegram
↓
/v1/chat/completions

## Что изменилось
| Компонент | Было | Стало |
|-----------|------|-------|
| Chat Model | Cloudflare напрямую | **FastAPI (OpenAI-прокси)** |
| Base URL | `api.cloudflare.com` | `46.17.102.81:8001/v1` |
| Модель | `@cf/qwen/qwen3-30b-a3b-fp8` | `fastapi-proxy` |

## Зачем это нужно
1. **Централизация** — вся AI-логика в FastAPI
2. **Валидация** — Pydantic проверяет запросы
3. **Гибкость** — можно сменить модель без n8n
4. **Production** — n8n оркестрирует, FastAPI делает AI

## Проблемы и решения
- **404 MODEL_NOT_FOUND** — `Use Responses API` был включён → выключили
- **404 /v1/models** — не было эндпоинта → добавили
- **`uuid` is not defined** — импорты были в конце файла → перенесли в начало

## Тест
- Запрос: «Что такое FastAPI?»
- Ответ: FastAPI-определение + источник
- Tokens: 1298
- Время: ~2 сек

## Файлы
- [main.py](./files/main.py)
- [.env.example](./files/.env.example)

## Следующий день
День 27: Тестирование API (pytest).