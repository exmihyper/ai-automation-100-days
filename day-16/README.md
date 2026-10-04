# День 16: Кэширование + Cloudflare Workers AI ✅

**Дата:** 5 октября 2026

## Что сделано
- [x] Добавлен **Redis** в docker-compose.yml
- [x] Создан workflow **«Search with Cache»**:
  - Execute Workflow Trigger → Redis Get → IF → (true) Edit Fields / (false) HTTP Request → Edit Fields1 → Redis1 (Set)
- [x] Redis-кэш работает: TTL 1 час
- [x] Groq заменён на **Cloudflare Workers AI** (нет лимитов TPM)
- [x] Модель: `@cf/qwen/qwen3-30b-a3b-fp8`
- [x] Бот отвечает через кэш + SearXNG + Cloudflare

## Архитектура кэша
[AI Agent] → [Call 'Search with Cache']
↓
[Execute Workflow Trigger: query]
↓
[Redis Get: search:query]
↓
[IF: propertyName not empty]
├── true → [Edit Fields: response] → ответ из кэша
└── false → [HTTP Request: SearXNG]
↓
[Edit Fields1: обрезка]
↓
[Redis1 Set: TTL 3600]


## Что изменилось
| Компонент | Было | Стало |
|-----------|------|-------|
| Chat Model | Groq (8 000 TPM) | **Cloudflare Qwen3 30B** (10 000 Neurons/день) |
| Лимит | 8 000 TPM | 10 000 Neurons/день (~200–500 запросов) |
| Кэш | Нет | **Redis с TTL 1 час** |

## Проблемы и решения
- **Groq постоянно упирался в лимит 8 000 TPM** → перешли на Cloudflare
- **Cloudflare через OpenAI Credential** не работал (`Method not allowed`) → установили community-ноду `n8n-nodes-cloudflare-ai`
- **Call n8n Workflow Tool не видел «Search with Cache»** → заменили Webhook на Execute Workflow Trigger
- **HTTP Request получал `null` из IF** → использовали `$('When Executed by Another Workflow').item.json.query`

## Тесты
- «Погода в Москве» → SearXNG через кэш, ответ за 33 сек
- «Что такое JOIN?» → SQL Tool (база)

## Стоимость
- **Cloudflare Workers AI:** бесплатно (10 000 Neurons/день)
- **Redis:** бесплатно (в Docker)
- **SearXNG:** бесплатно (свой сервер)
- **Ollama:** бесплатно (эмбеддинги)

## Файлы
- [workflow.json](./files/workflow.json)
- [workflow-search-with-cache.json](./files/workflow-search-with-cache.json)

## Следующий шаг
День 17: Fallback — база → интернет.