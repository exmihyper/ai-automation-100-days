from fastapi import FastAPI, HTTPException
from models import ChatRequest, ChatResponse, HealthResponse
from config import settings
import httpx

app = FastAPI(title="AI Automation API", version="0.3.0")

@app.get("/", response_model=HealthResponse)
async def root():
    return HealthResponse(status="ok", version="0.3.0")

@app.get("/health", response_model=HealthResponse)
async def health():
    return HealthResponse(status="healthy", version="0.3.0")

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    url = f"https://api.cloudflare.com/client/v4/accounts/{settings.CF_ACCOUNT_ID}/ai/v1/chat/com>
    
    headers = {
        "Authorization": f"Bearer {settings.CF_API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    messages = [{"role": "system", "content": "Ты — AI-ассистент. Отвечай кратко и по делу."}]
    if req.history:
        messages.extend([{"role": m.role.value, "content": m.content} for m in req.history])
    messages.append({"role": "user", "content": req.message})
    
    payload = {
        "model": settings.CF_MODEL,
        "messages": messages
    }
    
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(url, headers=headers, json=payload)
            resp.raise_for_status()
            data = resp.json()
            answer = data["choices"][0]["message"]["content"]
            usage = data.get("usage", {})
            return ChatResponse(
                answer=answer,
                model=settings.CF_MODEL,
                tokens_used=usage.get("total_tokens")
            )
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=502, detail=f"Cloudflare error: {e.response.status_code}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")