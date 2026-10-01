# День 14: Финализация недели 2 ✅

**Дата:** 2 октября 2026

## Что проверено
- [x] Три контейнера работают: n8n-main, n8n-runners, n8n-postgres
- [x] n8n открывается по HTTPS
- [x] `/joke` → шутка
- [x] «Что такое JOIN?» → SQL RAG
- [x] «А какие виды?» → память работает
- [x] «Что такое list comprehension?» → Python RAG
- [x] Смешанный вопрос → агент использует оба Tool
- [x] PostgreSQL хранит историю (session_id = 5642054503)
- [x] Error Handler ловит ошибки, уведомляет в Telegram

## Итоговая архитектура

[Telegram Trigger] → [IF1]
├── (true) → [HTTP Request] → [Telegram: шутка]
└── (false) → [AI Agent] → [Telegram: ответ]
↓ (Chat Model) ↓ (Memory) ↓ (Tools)
[Groq Chat Model] [Postgres] [SQL] [Python]
↓
[PostgreSQL]
n8n_chat_histories

[Error Trigger] → [Telegram: уведомление]


## Что умеет бот на конец недели 2
| Функция | Статус |
|---------|--------|
| `/joke` — шутки | ✅ |
| RAG по SQL | ✅ |
| RAG по Python | ✅ |
| AI Agent выбирает Tool | ✅ |
| Память диалога | ✅ |
| Multi-user (динамический Session ID) | ✅ |
| Очистка памяти (cron) | ✅ |
| Обработка ошибок | ✅ |
| Уведомления в Telegram | ✅ |

## Ретроспектива недели 2
**Что получилось:**
- Понял разницу Simple Memory vs PostgreSQL Memory
- Настроил динамический Session ID через `$json`
- Оптимизировал Context Window Length
- Настроил cron-очистку
- Разобрался с Error Workflow

**Что было сложно:**
- Session ID возвращал `undefined` → нашёл решение через `$json`
- Retry в AI-узлах недоступен → используем Error Workflow
- Cron не был установлен → установил

## Файлы
- [workflow.json](./files/workflow.json)

## Следующая неделя (3)
Веб-поиск и гибридный RAG:
- SerpAPI
- DuckDuckGo Search Tool
- Fallback: база → интернет