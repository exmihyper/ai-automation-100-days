# День 13: Обработка ошибок в памяти (retry, fallback, алерты) ✅

**Дата:** 1 октября 2026

## Что сделано
- [x] Создан **Error Handler** — отдельный workflow для ловли ошибок
- [x] Узел **Error Trigger** ловит ошибки из других workflow
- [x] Уведомление об ошибке приходит в Telegram
- [x] Error Handler подключён к основному workflow через Settings
- [x] Error Handler активирован (Publish)

## Архитектура Error Handler
[Error Trigger] → [Send a text message2]
↓
Telegram (уведомление)


## Настройка Error Workflow в основном workflow
1. Три точки → **Settings**
2. **Error Workflow** → выбрать **Error Handler**
3. **Save**

## Что делает Error Handler
- Ловит **любую ошибку** в основном workflow
- Отправляет уведомление в Telegram с:
  - Названием workflow
  - Узлом, где произошла ошибка
  - Текстом ошибки

## Тест (когда проведём)
1. Остановить PostgreSQL: `docker compose stop postgres`
2. Отправить боту сообщение
3. Должно прийти уведомление в Telegram
4. Запустить PostgreSQL: `docker compose start postgres`

## Ограничения n8n 2.x
- В AI-узлах (Groq Chat Model, Postgres Chat Memory) **нет встроенного Retry** в Settings
- Это нормально — Retry можно настроить только на некоторых узлах
- **Error Workflow** — основной инструмент устойчивости

## Файлы
- [workflow-main.json](./files/workflow-main.json)
- [workflow-error-handler.json](./files/workflow-error-handler.json)

## Следующий шаг
День 14: Финализация недели 2 — Memory + Agent + Tools в одном боте.