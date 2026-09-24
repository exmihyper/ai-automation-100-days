# День 7: AI Agent с Tools ✅

**Дата:** 24 сентября 2026

## Что сделано
- [x] Question and Answer Chain заменён на **AI Agent**
- [x] Добавлены **два инструмента** (Tools):
  - **SQL Tool** — Vector Store Tool с фильтром `source: sql`
  - **Python Tool** — Vector Store Tool с фильтром `source: python`
- [x] AI Agent **сам выбирает**, какой Tool использовать
- [x] System Message объясняет агенту, когда какой Tool применять
- [x] Groq Chat Model (`openai/gpt-oss-120b`) — быстрая генерация
- [x] Embeddings Ollama — векторизация (локально)

## Архитектура
[Telegram Trigger] → [IF1: /joke?]
├── (true) → [HTTP Request] → [Telegram: шутка]
└── (false) → [AI Agent] → [Telegram: ответ]
↓ (Chat Model) ↓ (Tools)
[Groq Chat Model] [SQL Tool] [Python Tool]
↓ ↓
[Simple VS] [Simple VS]
(source:sql) (source:python)
↓ ↓
[Embeddings] [Embeddings]


## Agentic AI — что это
- **Chain** (День 6): линейный поток, всегда одинаковый
- **Agent** (День 7): автономный, сам выбирает инструменты
- **Разница:** агент планирует, вызывает Tools, объединяет результаты

## Ключевые открытия
- **AI Agent** — узел для Agentic AI в n8n
- **Vector Store Tool** — обёртка над Simple Vector Store для агента
- **Description** — критично: агент читает описание и решает, использовать ли Tool
- **Metadata Filter** — фильтрует поиск по `source: sql` / `source: python`
- **Prompt (User Message)** — отдельное обязательное поле (как в Chain)
- **System Message** — инструкция для агента, когда какой Tool использовать

## Проблемы и решения
- `Parameter "Prompt (User Message)" is required` → переключил Source for Prompt на `Take from previous node automatically`, появилось поле Prompt
- Memory Key был `vector_store_key` → заменил на `knowledge_base`
- Метаданные не фильтровались → добавил Metadata Filter в каждый Tool

## Тесты
- «Что такое JOIN?» → агент использует **SQL Tool**
- «Что такое list comprehension?» → агент использует **Python Tool**
- «Сравни...» → агент использует **оба Tool**

## Файлы
- [workflow.json](./files/workflow.json)

## Следующий шаг
День 8: Память агента (Memory) — диалог с контекстом.