# День 3: RAG — База знаний ✅

**Дата:** 15 сентября 2026

## Что сделано
- [x] Установлен Ollama на сервер
- [x] Скачаны модели: nomic-embed-text (эмбеддинги), llama3.2:1b (генерация)
- [x] Настроен OLLAMA_HOST для доступа из Docker
- [x] Смонтирована папка /root/n8n-data в /home/node/.n8n-files
- [x] Создан документ knowledge.txt
- [x] Собран workflow «Загрузка документа»:
  - Manual Trigger → Read/Write Files → Simple Vector Store
  - Embeddings Ollama + Default Data Loader + Text Splitter
- [x] Собран workflow «Вопросы»:
  - Chat Trigger → Question and Answer Chain
  - Vector Store Retriever + Ollama Chat Model
- [x] RAG работает — бот отвечает по документу

## Архитектура RAG
1. **Загрузка:** документ → чанки (500 символов) → эмбеддинги → векторная база
2. **Поиск:** вопрос → эмбеддинг → поиск похожих чанков → контекст для модели
3. **Ответ:** модель генерирует ответ на основе найденных чанков

## Технологии
- **Ollama:** локальный запуск LLM без API-ключей и платежей
- **nomic-embed-text:** модель эмбеддингов (137M параметров)
- **llama3.2:1b:** модель генерации (1.2B параметров)
- **Simple Vector Store:** встроенная векторная база n8n
- **Memory Key:** `knowledge_base`

## Проблемы и решения
- n8n не видел файлы вне разрешённой папки → смонтировали в /home/node/.n8n-files
- Default Data Loader не добавляется напрямую → это под-узел Vector Store
- Vector Store Retriever создаёт свой Simple Vector Store → подключили к нему отдельный Embeddings

## Ограничения
- **Скорость:** ~1.5 минуты на ответ (CPU-only, 2 ГБ RAM)
- **Модель:** llama3.2:1b — маленькая, но достаточная для теста
- **Решение:** для продакшена — GPU-сервер или OpenAI API

## Следующий шаг
День 4: Интеграция RAG с Telegram-ботом (бот отвечает на вопросы по документу).