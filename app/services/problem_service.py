from app.domain.difficulty_level import DifficultyLevel
from app.entities.problem_entity import Problem
from app.repository.problem_repository import ProblemRepository
from app.dto.problems_dto import ProblemRequestDTO, ProblemResponseDTO
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
    def create_problem(self, request_dto: ProblemRequestDTO) -> ProblemResponseDTO:
        new_problem = self.map_to_new_problem(request_dto)
        self.repository.add(new_problem)
        return self.map_to_response_dto(new_problem)

    @staticmethod
    def map_to_new_problem(request_dto: ProblemRequestDTO) -> Problem:
        """ Not Sure if I like the Enum difficulty class """
        return Problem(request_dto.title, DifficultyLevel[request_dto.difficulty])

    @staticmethod
    def map_to_response_dto(problem: Problem) -> ProblemResponseDTO:
        """ Issue with accessing the entity itself, not to make sure this is secure """
        return ProblemResponseDTO(title=problem.title, difficulty=problem.difficulty, created_on=problem.created_on)