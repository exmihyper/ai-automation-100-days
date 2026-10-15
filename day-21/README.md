# День 21: Финализация недели 3 ✅

**Дата:** 15 октября 2026

## Итоги недели 3 (Дни 15–21)

### Что сделано
- [x] **День 15:** SearXNG — свой метапоисковик в Docker
- [x] **День 16:** Redis-кэш + переход на Cloudflare Workers AI
- [x] **День 17:** Fallback (база → интернет) + System Message с правилами
- [x] **День 18:** Гибридный поиск (RAG + Web) + TTL по типу запроса
- [x] **День 19:** Evaluation — LLM-as-a-Judge (средняя оценка 9.30/10)
- [x] **День 20:** Цитирование источников (SQL, Python, SearXNG)
- [x] **День 21:** Финализация — полный тест, README, защита от токенов

### Полный тест всех сценариев
| Тест | Запрос | Результат |
|------|--------|-----------|
| А | /joke | ✅ Шутка |
| Б | Что такое JOIN? | ✅ Ответ + 📚 SQL Tool |
| В | Что такое list comprehension? | ✅ Ответ + 📚 Python Tool |
| Г | Что такое Rust? | ✅ Ответ + 🌐 SearXNG URL |
| Д | А какие виды? | ✅ Помнит контекст |

### Метрики
- **5 контейнеров** работают: n8n, runners, postgres, searxng, redis
- **Redis:** ключи `search:*` создаются
- **PostgreSQL:** история диалогов сохраняется
- **Средняя оценка RAG:** 9.30/10

## Ретроспектива недели 3

### Что получилось
- SearXNG в Docker — бесплатный поиск без санкций
- Redis-кэш — повторные запросы мгновенные
- Cloudflare Workers AI — нет лимитов TPM (в отличие от Groq)
- LLM-as-a-Judge — объективные метрики качества
- Цитирование — прозрачность ответов

### Что было сложно
- **Groq упирался в лимит 8 000 TPM** → перешли на Cloudflare
- **Search1API/SerpAPI** не подошли → свой SearXNG
- **Call n8n Workflow Tool** не видел Webhook-workflow → заменили на Execute Workflow Trigger
- **Кодировка файла** eval_questions.txt сломалась → захардкодили в Code
- **Случайно закоммитили Cloudflare токен** → отозвали, добавили pre-commit hook

### Ключевые открытия
- **Execute Workflow Trigger** — для вызова workflow из другого workflow
- **`$('Node Name')`** — доступ к данным других узлов
- **Optimize Response** в HTTP Request — обрезка больших ответов
- **Cloudflare Workers AI** — OpenAI-совместимый API
- **pre-commit hook** — автопроверка на секреты

## Что дальше — Неделя 4 (Дни 22–28)

**Тема:** Python + FastAPI

- День 22: Python — основы FastAPI
- День 23: REST API для AI-сервисов
- День 24: Pydantic — валидация
- День 25: Async/await
- День 26: Интеграция FastAPI + n8n
- День 27: Тестирование API
- День 28: Финализация недели 4

## Файлы
- [workflow.json](./files/workflow.json) — основной workflow
- [workflow-search-with-cache.json](./files/workflow-search-with-cache.json)
- [workflow-evaluation.json](./files/workflow-evaluation.json)