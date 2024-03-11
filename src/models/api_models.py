from pydantic import BaseModel
from typing import Optional


class Input(BaseModel):
    message: str
    personality: str


class Result(BaseModel):
    answer: str


class Response(BaseModel):
    error: Optional[str]
    result: Optional[Result]
