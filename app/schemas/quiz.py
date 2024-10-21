from pydantic import BaseModel
from typing import List


class QuizQuestion(BaseModel):
    question: str
    options: List[str]
    answer: str


class QuizResponse(BaseModel):
    subject: str
    topic: str
    questions: List[QuizQuestion]
