# День 17: Fallback — база → интернет ✅

**Дата:** 7 октября 2026

## Что сделано
- [x] Обновлён **System Message** в AI Agent — чёткие правила выбора Tool
- [x] Fallback Model отключён (Cloudflare не имеет лимитов TPM)
- [x] Настроен трёхуровневый fallback:
  1. **SQL Tool** — вопросы по SQL
  2. **Python Tool** — вопросы по Python
  3. **Search with Cache** — вопросы вне базы (SearXNG)
  4. **Честное «не знаю»** — если нигде нет ответа

## System Message — правила выбора Tool
Ты — AI-ассистент с доступом к трём инструментам:

SQL Tool — база из 40 вопросов по SQL

Python Tool — база из 40 вопросов по Python

Search with Cache — веб-поиск через SearXNG

ПРАВИЛА:

Вопрос про SQL → SQL Tool

Вопрос про Python → Python Tool

Вопрос про оба → оба Tool

Вопрос вне базы → Search with Cache

Если нигде нет → честно «не знаю»


## Архитектура

[AI Agent]
↓ (Chat Model) ↓ (Memory) ↓ (Tools)
[Cloudflare] [Postgres] [SQL] [Python] [Search with Cache]


## Почему отключили Fallback
- **Cloudflare Workers AI** — 10 000 Neurons/день, без TPM-лимитов
- Fallback на **Ollama** (llama3.2:1b) был бы медленнее (1-2 мин на ответ)
- Cloudflare **стабилен** — не падает с rate limit, как Groq
- Ollama модель `llama3.2:1b` была удалена (осталась только `nomic-embed-text`)

## Тесты
| Тест | Вопрос | Ожидаемый Tool | Результат |
|------|--------|----------------|-----------|
| А | Что такое JOIN? | SQL Tool | ✅ |
| Б | Что такое list comprehension? | Python Tool | ✅ |
| В | Что такое Rust? | Search with Cache | ✅ |
| Г | Расскажи про квантовую физику | Честный ответ | ✅ |

## Файлы
- [workflow.json](./files/workflow.json)

## Следующий день
День 18: Гибридный поиск (RAG + Web) — оптимизация.