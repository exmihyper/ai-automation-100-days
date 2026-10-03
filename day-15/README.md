# День 15: SearXNG — гибридный RAG (база + интернет) ✅

**Дата:** 3 октября 2026

## Что сделано
- [x] Развёрнут **SearXNG** в Docker на своём сервере
- [x] Включён JSON-формат в `settings.yml`
- [x] SearXNG доступен из n8n по `http://searxng:8080`
- [x] Добавлен **HTTP Request Tool** к AI Agent
- [x] Настроены параметры: `q` (fromAI), `format=json`, `count=1`
- [x] Включён **Optimize Response** (оставляем только `title`, `url`, `content`)
- [x] Сокращён размер запроса: с 11 388 до ~6 500 токенов
- [x] **Гибридный RAG работает:** база → интернет



## docker-compose.yml — 4 сервиса
- `n8n` — оркестрация
- `n8n-runners` — Python + JS раннеры
- `postgres` — память диалогов
- **`searxng`** — веб-поиск (НОВЫЙ)

## Ключевые открытия
- **SearXNG** — метапоисковик с открытым исходным кодом, без API-ключей
- **`docker compose cp`** — копирование файлов между хостом и контейнером
- **Optimize Response** — встроенная обрезка ответа в HTTP Request Tool
- **`$fromAI()`** — функция n8n для передачи параметров от агента в Tool
- **Лимиты Groq:** 8 000 TPM на бесплатном тарифе — критично для больших ответов

## Проблемы и решения
- SerpAPI блокирует Россию → **SearXNG на своём сервере**
- Search1API не подключается → отказались
- DuckDuckGo узла нет в n8n → отказались
- Публичные SearXNG не дают JSON → **свой инстанс**
- Ответ SearXNG = 11 388 токенов → **Optimize Response + count=1**
- Rate limit Groq → снизили Context Window Length, Limit в Tools

## Тесты
- «Погода в Москве» → SearXNG (интернет)
- «Что такое JOIN?» → SQL Tool (база)
- «Что такое list comprehension?» → Python Tool (база)
- «Что такое Rust?» → SearXNG (интернет)

## Файлы
- [workflow.json](./files/workflow.json)

## Следующий шаг
День 16: Кэширование результатов поиска (чтобы не тратить токены на повторные запросы).