from app.domain.difficulty_level import DifficultyLevel
from app.entities.problem_entity import Problem
from app.repository.problem_repository import ProblemRepository
from typing import Optional


class ProblemService:
    def __init__(self, repository: ProblemRepository):
        self.repository = repository

    # find by id
    def get_problem(self, problem_id: int) -> Optional[Problem]:
        return self.repository.get_by_id(problem_id)

    # list all by difficulty
    def list_all_problems(self) -> list[type[Problem]]:
        return self.repository.list_all()

    # list all
    def list_all_by_difficulty(self, difficulty: DifficultyLevel) -> list[type[Problem]]:
        return self.repository.list_all_by_difficulty(difficulty)

    # create/post new
    def create_problem(self, problem: Problem) -> Problem:
        self.repository.add(problem)
        self.repository.commit()
        return problem