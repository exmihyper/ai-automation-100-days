# День 8: Память агента (Simple Memory) ✅

**Дата:** 25 сентября 2026

## Что сделано
- [x] Добавлен узел **Simple Memory** к AI Agent
- [x] Session ID настроен (Fixed: `5642054503` для теста)
- [x] Context Window Length = 10 сообщений
- [x] Агент помнит контекст диалога
- [x] Проверен диалог: «Что такое JOIN?» → «А какие виды?» — помнит

## Архитектура
[Telegram Trigger] → [IF1: /joke?]
├── (true) → [HTTP Request] → [Telegram: шутка]
└── (false) → [AI Agent] → [Telegram: ответ]
↓ (Chat Model) ↓ (Memory) ↓ (Tools)
[Groq Chat Model] [Simple Memory] [SQL Tool] [Python Tool]


## Как работает память
- **Session ID** — ключ, по которому память привязывается к пользователю
- **Context Window Length** — сколько последних сообщений помнить (10)
- **Simple Memory** — хранит данные в оперативной памяти n8n (без БД)

## Ограничения Simple Memory
- **Не персистентна:** при перезапуске n8n память обнуляется
- **Не работает с multi-instance:** если n8n в кластере, память не шарится между воркерами
- **Для production:** рекомендуется PostgreSQL/Redis Memory

## Проблемы и решения
- `Key parameter is empty` → Expression `$('Telegram Trigger').item.json.message.chat.id` возвращал `undefined`
- **Решение:** переключил Session ID на **Fixed** и ввёл ID вручную (`5642054503`) для теста
- **На будущее:** для production — динамический Session ID из Chat Trigger или PostgreSQL

## Тесты
- «Что такое JOIN?» → ответ по SQL
- «А какие виды?» → агент помнит, отвечает про INNER/LEFT/RIGHT/FULL/CROSS
- «А что такое list comprehension?» → переключился на Python

## Файлы
- [workflow.json](./files/workflow.json)

## Следующий шаг
День 9: PostgreSQL Chat Memory — персистентная память, переживает перезапуск.