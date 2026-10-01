# 🧠 AI Automation: 100 дней погружения

**Дневник и портфолио пути в AI Automation Engineer**

---

## 🎯 Цель

Стать AI Automation Engineer: уметь проектировать и внедрять агентные системы в бизнесе.

**Стек:** n8n · Ollama · Groq · PostgreSQL · Telegram API · Docker · Nginx · Let's Encrypt

---

## 🗺️ Дорожная карта

| Неделя | Дни | Тема | Статус |
|--------|-----|------|--------|
| 1 | 1–7 | Инфраструктура + RAG + Agentic AI | ✅ |
| 2 | 8–14 | Память и диалог | 🔄 |
| 3 | 15–21 | Веб-поиск и гибридный RAG | ⬜ |
| 4 | 22–28 | Python + FastAPI | ⬜ |
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

## 📊 Прогресс

![Progress](https://progress-bar.dev/13/?scale=100&title=days&width=400)

**Пройдено: 13 из 100 дней**

---

## 📁 Структура
├── day-01/ # Первая шутка на Python (n8n + HTTP Request + Code)
├── day-02/ # Telegram Joke Bot на VPS с HTTPS
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
├── docker-compose.yml # n8n + runners + PostgreSQL
└── README.md # Ты здесь


---

## 🛠️ Что построено

### Telegram-бот `@joke_day_2026_bot`
- `/joke` → шутки Чака Норриса
- Вопросы по SQL → RAG по 40 вопросам
- Вопросы по Python → RAG по 40 вопросам
- AI Agent сам выбирает инструмент
- Помнит диалог (PostgreSQL, 5 сообщений)
- Работает 24/7 на сервере Hostkey (Нидерланды)

### Инфраструктура
- VPS: Hostkey, 2 ГБ RAM, 60 ГБ SSD, Ubuntu 24.04
- Docker Compose: n8n + runners + PostgreSQL 16
- Nginx + Let's Encrypt (HTTPS)
- Домен: `n8n-turbomurzik.46.17.102.81.sslip.io`

### Технологии
- **n8n 2.22.4** — оркестрация
- **Groq** (`openai/gpt-oss-120b`) — быстрая генерация
- **Ollama** (`nomic-embed-text`) — эмбеддинги
- **PostgreSQL 16** — память диалогов
- **Telegram API** — интерфейс

---

## 🎯 Ключевые вехи

- ✅ **День 7** — RAG + Agentic AI
- ✅ **День 10** — Динамический Session ID (multi-user)
- ✅ **День 13** — Обработка ошибок
- 🔜 **День 14** — Финализация недели 2
- ⬜ **День 21** — Веб-поиск
- ⬜ **День 28** — Python + FastAPI
- ⬜ **День 100** — AI Automation Engineer

---

## 📝 Правила игры

1. Каждый день — новая папка `day-XX` с README и workflow.json
2. Честность: трудности и неудачные попытки — тоже часть пути
3. Каждую неделю — ретроспектива
4. Всё важное — в GitHub (бэкап + портфолио)

---

**Старт:** 11 сентября 2026
**Финиш:** 19 декабря 2026
