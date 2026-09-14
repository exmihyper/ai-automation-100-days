# День 2: Telegram Joke Bot на сервере ✅

**Дата:** 14 сентября 2026

## Что сделано
- [x] Куплен VPS Hostkey (Нидерланды, 2 ГБ RAM, 60 ГБ SSD)
- [x] Установлен Docker + Docker Compose на сервере
- [x] Создан swap-файл 2 ГБ
- [x] Настроен домен sslip.io + Nginx + Let's Encrypt (HTTPS)
- [x] Запущен n8n 24/7 на сервере
- [x] Подключены Python и JavaScript раннеры
- [x] Telegram Trigger принимает сообщения
- [x] Команда `/joke` → шутка из API
- [x] Другие сообщения → подсказка
- [x] Авто-рассылка каждый день в 9:00

## Архитектура
- **Сервер:** Hostkey VPS (46.17.102.81)
- **Домен:** n8n-turbomurzik.46.17.102.81.sslip.io
- **SSL:** Let's Encrypt (автопродление)
- **Reverse proxy:** Nginx
- **n8n:** 2.22.4 в Docker Compose
- **Раннеры:** Python + JavaScript

## Проблемы и решения
- ngrok блокирует РФ по IP → отказались
- Cloudflare quick tunnel рвёт соединение → отказались
- localtunnel требует пароль → отказались
- Serveo порты 80/443 заняты → отказались
- Cloudcore/Hostora закрывают порты → вернули деньги
- Hostkey: SSH не работал с первого IP → сменили IP через панель
- Telegram требует HTTPS → настроили Nginx + Let's Encrypt + sslip.io

## Файлы
- [workflow.json](./files/workflow.json)

## Следующий шаг
День 3: RAG — база знаний и умный поиск по документам.