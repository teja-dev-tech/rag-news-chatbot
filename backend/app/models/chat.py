from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional, Dict, Any

class Message(BaseModel):
    role: str  # 'user' or 'assistant'
    content: str
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    session_id: str
    reply: str
    sources: List[Dict[str, str]] = []

class ChatHistory(BaseModel):
    session_id: str
    messages: List[Message]
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())