# День 24: Pydantic — валидация данных ✅

**Дата:** 26 октября 2026

## Что сделано
- [x] Создан `models.py` с расширенными Pydantic-моделями
- [x] **Enum** для роли сообщения (`user`, `assistant`, `system`)
- [x] **Вложенные модели** (`Message` внутри `ChatRequest`)
- [x] **Field с ограничениями** (`min_length`, `max_length`, `ge`, `le`)
- [x] **`@field_validator`** — проверка, что сообщение не пустое
- [x] **`@model_validator(mode="after")`** — проверка длины истории (≤ 20)
- [x] **`response_model`** — валидация ответа (HealthResponse, ChatResponse)
- [x] Обновлён `main.py` (версия 0.3.0)
- [x] Тесты: валидный → 200, невалидный → 422

## Модели в `models.py`
```python
class MessageRole(str, Enum):
    user = "user"
    assistant = "assistant"
    system = "system"

class Message(BaseModel):
    role: MessageRole
    content: str = Field(..., min_length=1, max_length=2000)

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=500)
    temperature: float = Field(default=0.7, ge=0.0, le=1.0)
    max_tokens: int = Field(default=500, ge=10, le=2000)
    history: Optional[list[Message]] = None

    @field_validator("message")
    @classmethod
    def message_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Сообщение не может быть пустым")
        return v.strip()

    @model_validator(mode="after")
    def check_history_length(self):
        if self.history and len(self.history) > 20:
            raise ValueError("История не может быть длиннее 20 сообщений")
        return self