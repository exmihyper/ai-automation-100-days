# День 27: Тестирование API (pytest) ✅

**Дата:** 5 ноября 2026

## Что сделано
- [x] Установлен `pytest`, `pytest-asyncio`, `httpx`
- [x] Создан `test_main.py` с 8 тестами
- [x] Тесты для `/`, `/health` — базовые
- [x] Тесты для `/chat` — валидный, пустой, длинный
- [x] Тесты для `/v1/models` — список моделей
- [x] Тесты для `/v1/chat/completions` — OpenAI-совместимый
- [x] Все 8 тестов **PASSED** за 13 секунд

## Что тестируется
| Тест | Что проверяет |
|------|---------------|
| `test_root` | `GET /` → 200, status=ok |
| `test_health` | `GET /health` → 200, status=healthy |
| `test_chat_valid` | `POST /chat` → 200, есть answer |
| `test_chat_empty_message` | Пустое сообщение → 422 |
| `test_chat_too_long_message` | Длинное сообщение → 422 |
| `test_list_models` | `GET /v1/models` → 200, есть fastapi-proxy |
| `test_openai_compat_valid` | `POST /v1/chat/completions` → 200, есть choices |
| `test_openai_compat_no_messages` | Нет messages → 422 |

## Запуск тестов
```bash
cd /root/fastapi-app
source venv/bin/activate
pytest test_main.py -v