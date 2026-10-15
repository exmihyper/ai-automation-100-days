# 🧠 AI Automation: 100 дней погружения

**Дневник и портфолио пути в AI Automation Engineer**

---

## 🎯 Цель

Стать AI Automation Engineer: уметь проектировать и внедрять агентные системы в бизнесе.

**Стек:** n8n · Ollama · Cloudflare · PostgreSQL · Redis · SearXNG · Telegram API · Docker · Nginx

---

## 📊 Прогресс

**Пройдено: 21 из 100 дней**

| Неделя | Дни | Тема | Статус |
|--------|-----|------|--------|
| 1 | 1–7 | Инфраструктура + RAG + Agentic AI | ✅ |
| 2 | 8–14 | Память и диалог | ✅ |
| 3 | 15–21 | Веб-поиск и гибридный RAG | ✅ |
| 4 | 22–28 | Python + FastAPI | 🔄 |
| 5 | 29–35 | PostgreSQL + БД | ⬜ |
| 6 | 36–42 | Мульти-агентные системы | ⬜ |
| 7 | 43–49 | LangChain глубоко | ⬜ |
| 8 | 50–56 | Продвинутый RAG | ⬜ |
| 9 | 57–63 | Evaluation + Guardrails | ⬜ |
| 10 | 64–70 | Production: мониторинг, CI/CD | ⬜ |
| 11 | 71–77 | Масштабирование | ⬜ |
| 12 | 78–84 | Безопасность | ⬜ |
| 13 | 85–91 | Проект 1: HR-бот | ⬜ |
| 14 | 92–98 | Проект 2: Мультиагентная система | ⬜ |
| Финал | 99–100 | Портфолио, резюме, собеседования | ⬜ |

---

## 📁 Структура
├── day-01/ # Первая шутка на Python
├── day-02/ # Telegram Joke Bot на VPS
├── day-03/ # RAG — база знаний на Ollama
├── day-04/ # RAG в Telegram
├── day-05/ # Объединённый умный бот
├── day-06/ # Мульти-документный RAG + Groq
├── day-07/ # AI Agent с Tools (Agentic AI)
├── day-08/ # AI Agent с памятью (Simple Memory)
├── day-09/ # PostgreSQL Chat Memory
├── day-10/ # Динамический Session ID
├── day-11/ # Context Window Optimization
├── day-12/ # Очистка памяти, TTL, cron
├── day-13/ # Обработка ошибок, Error Handler
├── day-14/ # Финализация недели 2
├── day-15/ # SearXNG — свой веб-поиск
├── day-16/ # Redis-кэш + Cloudflare Workers AI
├── day-17/ # Fallback (база → интернет)
├── day-18/ # Гибридный поиск (RAG + Web)
├── day-19/ # Evaluation — LLM-as-a-Judge
├── day-20/ # Цитирование источников
├── docker-compose.yml # 5 сервисов: n8n, runners, postgres, searxng, redis
└── README.md # Ты здесь

---

## 🛠️ Что построено

### Telegram-бот `@joke_day_2026_bot`
- `/joke` → шутки Чака Норриса
- SQL-вопросы → RAG по 40 вопросам (📚 Источник: SQL Tool)
- Python-вопросы → RAG по 40 вопросам (📚 Источник: Python Tool)
- Вопросы вне базы → SearXNG (🌐 Источник: [сайт])
- AI Agent сам выбирает инструмент
- Помнит диалог (PostgreSQL, динамический Session ID)
- Кэш Redis (TTL по типу запроса)
- Цитирование источников
- Error Handler (уведомления в Telegram)
- **Средняя оценка качества: 9.30/10**

### Инфраструктура
- **VPS:** Hostkey, 2 ГБ RAM, 60 ГБ SSD, Ubuntu 24.04
- **Docker Compose:** 5 сервисов (n8n, runners, postgres, searxng, redis)
- **Nginx + Let's Encrypt:** HTTPS
- **Домен:** `n8n-turbomurzik.46.17.102.81.sslip.io`

### Технологии
- **n8n 2.22.4** — оркестрация
- **Cloudflare Workers AI** (`@cf/qwen/qwen3-30b-a3b-fp8`) — генерация
- **Ollama** (`nomic-embed-text`) — эмбеддинги
- **PostgreSQL 16** — память диалогов
- **Redis 7** — кэш веб-поиска
- **SearXNG** — свой метапоисковик
- **Telegram API** — интерфейс

---

## 📈 Ключевые вехи

- ✅ **День 7** — RAG + Agentic AI
- ✅ **День 10** — Динамический Session ID (multi-user)
- ✅ **День 13** — Обработка ошибок
- ✅ **День 16** — Redis-кэш + Cloudflare (без лимитов)
- ✅ **День 19** — Evaluation (9.30/10)
- ✅ **День 20** — Цитирование источников
- 🔜 **День 28** — Python + FastAPI
- ⬜ **День 100** — AI Automation Engineer

---

## 📝 Правила игры

1. Каждый день — новая папка `day-XX` с README и workflow.json
2. Честность: трудности — тоже часть пути
3. Всё важное — в GitHub (бэкап + портфолио)
4. **Никаких токенов в коммитах** (pre-commit hook + .gitignore)

---

**Старт:** 11 сентября 2026
**Финиш:** 19 декабря 2026