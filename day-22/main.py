from fastapi import FastAPI

app = FastAPI(title="AI Automation API", version="0.1.0")

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI on VPS!", "status": "ok"}

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "ai-automation-api"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}