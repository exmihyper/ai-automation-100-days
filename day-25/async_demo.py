import asyncio
import time
import httpx

async def fake_request(name: str, delay: float) -> str:
    """Имитация запроса с задержкой."""
    await asyncio.sleep(delay)
    return f"Result from {name} (after {delay}s)"

async def sync_way():
    """Последовательно — блокируемся на каждом запросе."""
    print("=== SYNC (последовательно) ===")
    start = time.time()
    
    result1 = await fake_request("A", 2.0)
    result2 = await fake_request("B", 2.0)
    result3 = await fake_request("C", 2.0)
    
    elapsed = time.time() - start
    print(f"Результаты: {result1}, {result2}, {result3}")
    print(f"Время: {elapsed:.2f} сек\n")
    return elapsed

async def async_way():
    """Параллельно — все запросы одновременно."""
    print("=== ASYNC (параллельно) ===")
    start = time.time()
    
    results = await asyncio.gather(
        fake_request("A", 2.0),
        fake_request("B", 2.0),
        fake_request("C", 2.0),
    )
    
    elapsed = time.time() - start
    print(f"Результаты: {results}")
    print(f"Время: {elapsed:.2f} сек\n")
    return elapsed

async def main():
    sync_time = await sync_way()
    async_time = await async_way()
    
    print(f"=== ИТОГ ===")
    print(f"Sync: {sync_time:.2f} сек")
    print(f"Async: {async_time:.2f} сек")
    print(f"Ускорение: {sync_time / async_time:.1f}x")

if __name__ == "__main__":
    asyncio.run(main())
