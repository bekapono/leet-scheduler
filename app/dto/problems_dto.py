from app.domain import difficulty_level
from app.domain.difficulty_level import DifficultyLevel
from datetime import datetime
from pydantic import BaseModel


class ProblemRequestDTO(BaseModel):
    title: str
    difficulty: str


class ProblemResponseDTO(BaseModel):
    title: str
    difficulty: DifficultyLevel
    created_on: datetime


class ProblemUpdateDTO(BaseModel):
    title: str
    difficulty: str

