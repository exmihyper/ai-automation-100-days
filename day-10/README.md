# День 10: Динамический Session ID для multi-user памяти ✅

**Дата:** 27 сентября 2026

## Что сделано
- [x] Session Key изменён с Fixed (`5642054503`) на Expression (`{{ $json.message.chat.id }}`)
- [x] Dynamic Session ID работает — значение подставляется автоматически
- [x] Память привязана к каждому пользователю отдельно
- [x] Проверено через psql: 22 сообщения для session_id = 5642054503
- [x] Multi-user готовность: бот поддерживает неограниченное число пользователей

## Архитектура

[Telegram Trigger] → [IF1] → (false) → [AI Agent] → [Send a text message1]
↓ (Memory)
[Postgres Memory]
Session Key = {{ $json.message.chat.id }}
↓
[PostgreSQL]
n8n_chat_histories
session_id | count
5642054503 | 22


## Разница Fixed vs Dynamic Session ID
| | Fixed (День 9) | Dynamic (День 10) |
|---|---|---|
| Session ID | `5642054503` | `{{ $json.message.chat.id }}` |
| Пользователей | 1 | Неограниченно |
| История | Смешивается | Изолирована |
| Production | ❌ | ✅ |

## Ключевое открытие
**`$json.message.chat.id`** работает, а **`$('Telegram Trigger').item.json.message.chat.id`** — нет.
- Причина: Postgres Chat Memory вызывается внутри AI Agent, и в этот момент данные передаются через `$json`, а не через ссылку на прошлый узел.
- Решение: использовать `$json` для текущего узла.

## Проверка multi-user
```bash
docker compose exec postgres psql -U n8n -d n8n_memory -c "SELECT session_id, COUNT(*) FROM n8n_chat_histories GROUP BY session_id;"