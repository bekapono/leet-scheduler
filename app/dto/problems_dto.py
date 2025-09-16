from app.domain.difficulty_level import DifficultyLevel
from datetime import datetime


class ProblemRequestDTO:
    def __init__(self, title: str, difficulty: str) -> None:
        self.__title = title
        self.__difficulty = difficulty

    def get_title(self) -> str:
        return self.__title

    def get_difficulty(self) -> str:
        return self.__difficulty


class ProblemResponseDTO:
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


class ProblemsUpdateDTO:
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

