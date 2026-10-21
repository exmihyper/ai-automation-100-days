from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from config import settings
import httpx

app = FastAPI(title="AI Automation API", version="0.2.0")

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=500)

class ChatResponse(BaseModel):
    answer: str
    model: str

@app.get("/")
async def root():
    return {"message": "AI Automation API", "version": "0.2.0"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    url = f"https://api.cloudflare.com/client/v4/accounts/{settings.CF_ACCOUNT_ID}/ai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {settings.CF_API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": settings.CF_MODEL,
        "messages": [
            {"role": "system", "content": "Ты — AI-ассистент. Отвечай кратко и по делу."},
            {"role": "user", "content": req.message}
        ]
    }
    
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(url, headers=headers, json=payload)
            resp.raise_for_status()
            data = resp.json()
            answer = data["choices"][0]["message"]["content"]
            return ChatResponse(answer=answer, model=settings.CF_MODEL)
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=502, detail=f"Cloudflare error: {e.response.status_code}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")