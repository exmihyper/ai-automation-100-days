# День 1: Первая шутка на Python ✅

**Дата:** 12 сентября 2026

## Что сделано
- [x] Запущен n8n 2.22.4 через Docker Compose
- [x] Настроен Python-раннер в external mode
- [x] Создан первый workflow: Manual Trigger → HTTP Request → Code in Python
- [x] Подключение к API chucknorris.io
- [x] Обработка JSON на Python
- [x] Workflow сохранён и экспортирован

## Новые узлы
- Manual Trigger
- HTTP Request
- Code in Python

## Ключевые открытия
- В n8n 2.x Python работает через внешний раннер
- Переменные в Python-узле: `_items` (все элементы) и `_item` (текущий)
- Формат возврата данных: `[{"json": {...}}]`
- Данные между узлами передаются как массив объектов

## Сложности
- Официальный образ n8n не содержит Python
- Решение: Docker Compose с двумя сервисами (n8n + n8n-runners)
- Синтаксис Python-узла отличается от JavaScript

## Файлы
- [workflow.json](./files/workflow.json) — экспорт workflow

## Завтра
День 2: Telegram-бот, Webhook, IF, авто-расписание.