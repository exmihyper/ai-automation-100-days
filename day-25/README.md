# День 25: Async/await в Python ✅

**Дата:** 29 октября 2026

## Что сделано
- [x] Создан `async_demo.py` — демонстрация sync vs async
- [x] Понята разница: sync блокируется, async — нет
- [x] Использован `asyncio.gather` для параллельных запросов
- [x] Добавлен эндпоинт `POST /chat/multi` — 3 параллельных запроса к Cloudflare
- [x] Ускорение в 3 раза: sync ~6 сек → async ~2 сек
- [x] Понята разница между `async def` и `def` в FastAPI

## Что такое async/await
- **`async def`** — объявляет асинхронную функцию (корутину)
- **`await`** — приостанавливает выполнение до завершения промиса
- **`asyncio.gather`** — запускает несколько корутин **параллельно**

## Sync vs Async (демо)
=== SYNC (последовательно) ===
Результаты: A, B, C
Время: 6.00 сек

=== ASYNC (параллельно) ===
Результаты: [A, B, C]
Время: 2.00 сек

Ускорение: 3.0x


## Код `/chat/multi`
```python
@app.post("/chat/multi")
async def chat_multi(req: ChatRequest):
    async def ask_cloudflare(temperature: float) -> dict:
        # ... запрос к Cloudflare
        return {"temperature": temperature, "answer": data["choices"][0]["message"]["content"]}
    
    results = await asyncio.gather(
        ask_cloudflare(0.1),
        ask_cloudflare(0.5),
        ask_cloudflare(0.9),
    )
    return {"answers": results}