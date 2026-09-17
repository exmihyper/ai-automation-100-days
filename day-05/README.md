# День 5: Объединённый умный бот (Joke + SQL RAG) ✅

**Дата:** 17 сентября 2026

## Что сделано
- [x] Объединены два workflow в один: Joke Bot + RAG
- [x] В False-ветке IF — Question and Answer Chain (RAG по SQL-документу)
- [x] В True-ветке IF — HTTP Request с шутками Чака Норриса
- [x] Загружен SQL-документ (40 вопросов по SQL) в векторную базу
- [x] 768 чанков из SQL-документа в Simple Vector Store
- [x] Бот отвечает на /joke шуткой
- [x] Бот отвечает на вопросы по SQL из документа

## Архитектура

[Telegram Trigger] → [IF: /joke?]
├── (true) → [HTTP Request] → [Telegram: шутка]
└── (false) → [Question and Answer Chain] → [Telegram: RAG]
↓ (Model) ↓ (Retriever)
[Ollama Chat Model] [Vector Store Retriever]
↓
[Simple Vector Store]
↓
[Embeddings Ollama]


## Новая база знаний
- **SQL-Academy-Interview-Questions-ru.pdf** — 40 вопросов по SQL
- Извлечён текст через `pdftotext -layout`
- Загружен в `knowledge_base` через workflow «RAG — Загрузка документа»

## Тесты
- `/joke` → шутка про Чака Норриса
- «Что такое JOIN?» → ответ по SQL-документу
- «Разница между WHERE и HAVING?» → ответ по документу

## Ключевые выводы
- **Один Telegram Webhook = один активный workflow** → нужно объединять
- **IF разделяет логику**: команды vs свободные вопросы
- **RAG расширяется**: можно загружать любые документы (.txt)
- **PDF → txt**: через `pdftotext -layout`

## Файлы
- [workflow.json](./files/workflow.json)

## Следующий шаг
День 6: Расширение базы знаний (несколько документов) + работа с метаданными.