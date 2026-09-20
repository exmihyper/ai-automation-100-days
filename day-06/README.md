# День 6: Мульти-документный RAG + Groq ✅

**Дата:** 20 сентября 2026

## Что сделано
- [x] Загружен SQL-документ (40 вопросов по SQL) в векторную базу
- [x] Загружен Python-документ (40 вопросов по Python)
- [x] Добавлены метаданные `source: sql` и `source: python` к чанкам
- [x] Настроена фильтрация по метаданным в Vector Store Retriever
- [x] Заменён Ollama Chat Model на Groq Chat Model
- [x] Скорость ответа: с 1–2 минут до 1–3 секунд (**ускорение в 200–400 раз**)
- [x] Embeddings остались на Ollama (`nomic-embed-text`) — быстро и локально
- [x] Бот отвечает и по SQL, и по Python

## Архитектура

[Telegram Trigger] → [IF: /joke?]
├── (true) → [HTTP Request] → [Telegram: шутка]
└── (false) → [Question and Answer Chain] → [Telegram: RAG]
↓ (Model) ↓ (Retriever)
[Groq Chat Model] [Vector Store Retriever]
↓
[Simple Vector Store]
↓
[Embeddings Ollama]


## Технологии
- **Groq Chat Model** (`openai/gpt-oss-120b`) — быстрая генерация ответов
- **Embeddings Ollama** (`nomic-embed-text`) — векторизация (локально)
- **Simple Vector Store** — база знаний в памяти
- **Metadata Filter** — фильтрация по `source: sql` / `source: python`

## Ключевые открытия
- **PDF → txt:** через `pdftotext -layout "file.pdf" output.txt`
- **Метаданные:** добавляются в узле Default Data Loader
- **Фильтрация:** в Vector Store Retriever через Metadata Filter
- **Groq:** бесплатный тариф с лимитами (30 RPM, 1000 RPD на модель)
- **Скорость:** Groq в 200–400 раз быстрее Ollama на CPU

## Проблемы и решения
- Ollama работал 1–2 минуты на ответ → перешли на Groq
- Groq отключил старые модели (`llama3-8b-8192`) → используем `openai/gpt-oss-120b`
- Simple Vector Store обнуляется при рестарте → загружаем документы после перезапуска n8n

## Файлы
- [workflow.json](./files/workflow.json)

## Следующий шаг
День 7: Query Routing — бот сам определяет, к какому документу обратиться.