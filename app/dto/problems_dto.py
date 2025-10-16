from app.domain import difficulty_level
from app.domain.difficulty_level import DifficultyLevel
from datetime import datetime, date
from pydantic import BaseModel


class ProblemRequestDTO(BaseModel):
    number: int
    title: str
    difficulty: str


class NewProblemResponseDTO(BaseModel):
    id: int
    problem_number: int
    title: str
    difficulty: DifficultyLevel
    dates: list[str] = []  # Default to empty list instead of requiring it
    created_on: datetime


class ProblemUpdateDTO(BaseModel):
    title: str
    difficulty: str

