from pydantic import BaseModel
from typing import Optional


class Input(BaseModel):
    """Input model for the chat endpoint."""
    message: str
    personality: str


class Result(BaseModel):
    """Result model for the chat endpoint."""
    answer: str


class Response(BaseModel):
    """Response model for the chat endpoint."""
    error: Optional[str]
    result: Optional[Result]
