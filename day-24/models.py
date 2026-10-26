from pydantic import BaseModel, Field, field_validator, model_validator
from enum import Enum
from typing import Optional

class MessageRole(str, Enum):
    user = "user"
    assistant = "assistant"
    system = "system"

class Message(BaseModel):
    role: MessageRole
    content: str = Field(..., min_length=1, max_length=2000)
    
class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=500, description="Вопрос пользователя")
    temperature: float = Field(default=0.7, ge=0.0, le=1.0, description="Креативность (0-1)")
    max_tokens: int = Field(default=500, ge=10, le=2000, description="Максимум токенов в ответе")
    history: Optional[list[Message]] = Field(default=None, description="История диалога")

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
    
    class ChatResponse(BaseModel):
    answer: str
    model: str
    tokens_used: Optional[int] = None

class HealthResponse(BaseModel):
    status: str
    version: str
class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=500, description="Вопрос пользователя")
    temperature: float = Field(default=0.7, ge=0.0, le=1.0, description="Креативность (0-1)")
    max_tokens: int = Field(default=500, ge=10, le=2000, description="Максимум токенов в ответе")
    history: Optional[list[Message]] = Field(default=None, description="История диалога")

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