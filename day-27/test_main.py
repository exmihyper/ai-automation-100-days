import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# ---------- Базовые тесты ----------
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


# ---------- Тесты /chat ----------
def test_chat_valid():
    response = client.post("/chat", json={"message": "Что такое FastAPI?"})
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert len(data["answer"]) > 0


def test_chat_empty_message():
    response = client.post("/chat", json={"message": "   "})
    assert response.status_code == 422
    assert "Сообщение не может быть пустым" in str(response.json())


def test_chat_too_long_message():
    response = client.post("/chat", json={"message": "x" * 501})
    assert response.status_code == 422


# ---------- Тесты /v1/models ----------
def test_list_models():
    response = client.get("/v1/models")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0
    assert data["data"][0]["id"] == "fastapi-proxy"


# ---------- Тесты /v1/chat/completions ----------
def test_openai_compat_valid():
    response = client.post(
        "/v1/chat/completions",
        json={
            "model": "fastapi-proxy",
            "messages": [{"role": "user", "content": "Что такое Pydantic?"}]
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "choices" in data
    assert data["choices"][0]["message"]["role"] == "assistant"
    assert len(data["choices"][0]["message"]["content"]) > 0


def test_openai_compat_no_messages():
    response = client.post(
        "/v1/chat/completions",
        json={"model": "fastapi-proxy"}
    )
    assert response.status_code == 422