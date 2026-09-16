# День 4: RAG в Telegram ✅

**Дата:** 16 сентября 2026

## Что сделано
- [x] Создан workflow «День 4 — RAG Telegram»
- [x] Telegram Trigger принимает сообщения
- [x] Question and Answer Chain обрабатывает вопросы
- [x] Vector Store Retriever ищет в базе knowledge_base
- [x] Simple Vector Store хранит 768 чанков
- [x] Ollama Chat Model (llama3.2:1b) генерирует ответы
- [x] Workflow выполнился успешно

## Архитектура
Telegram Trigger → Question and Answer Chain → Send a text message
                          ↓ (Model)         ↓ (Retriever)
                    Ollama Chat Model    Vector Store Retriever
                                                ↓
                                          Simple Vector Store
                                                ↓
                                          Embeddings Ollama

## Ключевые проблемы и решения
- **Prompt (User Message) обязателен** в режиме `Define below` — без него workflow не запускается
- **Simple Vector Store нельзя тестировать вручную** (`Execute step`) — только через Chain
- **AI-узлы работают только в связке**, не по отдельности
- **Telegram разрешает один Webhook на бота** → нужен объединённый workflow

## Ограничение (нерешённое)
- Telegram Webhook конфликтует между «Telegram Joke Bot» и «RAG Telegram»
- Решение в День 5: объединить шутки + RAG в один workflow

## Файлы
- [workflow.json](./files/workflow.json)

## Следующий шаг
День 5: Объединение Joke Bot + RAG в единый workflow с IF-ветвлением.