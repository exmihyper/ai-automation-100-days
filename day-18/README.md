# День 18: Гибридный поиск (RAG + Web) ✅

**Дата:** 8 октября 2026

## Что сделано
- [x] Проверена стабильность схемы: SQL Tool + Python Tool + Search with Cache
- [x] Настроен **TTL по типу запроса** в Redis:
  - «погода» → TTL 1 час (3600 сек)
  - остальное → TTL 1 день (86400 сек)
- [x] Fallback отключён (Cloudflare стабилен)
- [x] Протестированы 4 сценария: SQL, Python, интернет, кэш

## Архитектура
[Telegram Trigger] → [IF1] → (true) HTTP Request (шутка)
→ (false) → AI Agent → Send a message
↓ (Chat Model) ↓ (Memory) ↓ (Tools)
[Cloudflare] [Postgres] [SQL] [Python] [Search]
↓
[Search with Cache]
↓
[Redis Get] → [IF]
↓ true → ответ из кэша
↓ false → SearXNG → Redis Set