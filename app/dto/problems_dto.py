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


""" The class objects below don't work well with FastAPI so Pydantic models are needed """


class ProblemRequest:
    def __init__(self, title: str, difficulty: str) -> None:
        self.__title = title
        self.__difficulty = difficulty

    def get_title(self) -> str:
        return self.__title

    def get_difficulty(self) -> str:
        return self.__difficulty


class ProblemResponse:
    def __init__(self, title, difficulty: DifficultyLevel, created_on: datetime) -> None:
        self.__title = title
        self.__difficulty = difficulty
        self.__created_on = created_on

    def get_title(self) -> str:
        return self.__title

    def get_difficulty(self) -> DifficultyLevel:
        return self.__difficulty

    def get_created_on(self) -> datetime:
        return self.__created_on


class ProblemsUpdate:
    def __init__(self) -> None:
        self.__title = None
        self.__difficulty = None

    def get_title(self) -> str:
        return self.__title

    def get_difficulty(self) -> DifficultyLevel:
        return self.__difficulty

    def set_title(self, title: str) -> None:
        self.__title = title

    def set_difficulty(self, difficulty: DifficultyLevel) -> None:
        self.__difficulty = difficulty

