# День 9: PostgreSQL Chat Memory ✅

**Дата:** 26 сентября 2026

## Что сделано
- [x] Добавлен контейнер `postgres` в `docker-compose.yml`
- [x] PostgreSQL 16 Alpine запущен в Docker
- [x] База `n8n_memory` создана
- [x] Credential Postgres создан в n8n
- [x] Simple Memory заменён на **Postgres Chat Memory**
- [x] Таблица `n8n_chat_histories` создана автоматически
- [x] История диалогов сохраняется в БД
- [x] Память переживает перезапуск n8n

## Архитектура
[Telegram Trigger] → [IF1: /joke?]
├── (true) → [HTTP Request] → [Telegram: шутка]
└── (false) → [AI Agent] → [Telegram: ответ]
↓ (Chat Model) ↓ (Memory) ↓ (Tools)
[Groq Chat Model] [Postgres Memory] [SQL Tool] [Python Tool]
↓
[PostgreSQL]
n8n_memory
n8n_chat_histories


## Разница Simple Memory vs PostgreSQL Memory
| | Simple Memory | PostgreSQL Memory |
|---|---|---|
| Где хранит | Оперативная память n8n | База данных PostgreSQL |
| Переживает рестарт | ❌ Нет | ✅ Да |
| Multi-user | Ограниченно | ✅ Полностью |
| Production | ❌ Нет | ✅ Да |

## docker-compose.yml
Добавлен сервис `postgres`:
```yaml
postgres:
  image: postgres:16-alpine
  container_name: n8n-postgres
  restart: unless-stopped
  environment:
    - POSTGRES_USER=n8n
    - POSTGRES_PASSWORD=n8n_secure_password_2026
    - POSTGRES_DB=n8n_memory
  volumes:
    - postgres_data:/var/lib/postgresql/data
  healthcheck:
    test: ['CMD-SHELL', 'pg_isready -U n8n']