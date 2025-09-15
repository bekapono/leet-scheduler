from abc import ABC, abstractmethod
from typing import Optional, List, Any

from ..entities.problem_entity import Problem
from ..domain.difficulty_level import DifficultyLevel
from sqlalchemy.orm import Session

'''
    I'm getting confused with Problem entity, Problems table.
    Need to look up if SqlAlchemy query uses the entity? or table name.
'''


class ProblemRepository(ABC):
    @abstractmethod
    def get_by_id(self, problem_id: int) -> Optional[Problem]:
        pass

    @abstractmethod
    def list_all_by_difficulty(self, difficulty: DifficultyLevel) -> list[type[Problem]]:
        pass

    @abstractmethod
    def list_all(self) -> list[type[Problem]]:
        pass

    @abstractmethod
    def add(self, problem: Problem) -> None:
        pass


class SQLAlchemyProblemRepository(ProblemRepository, ABC):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(self, problem_id: int) -> Optional[Problem]:
        return self.session.query(Problem).filter(Problem.id == problem_id).first()

    def list_all_by_difficulty(self, difficulty: DifficultyLevel) -> list[type[Problem]]:
        return self.session.query(Problem).filter(Problem.difficulty == difficulty).all()
        # Having an issue with the return type. Want a list of problems, but
        # it's expecting a list[type[problem]].
        # Is there a difference between List[Type[Problem]] on the current solution.

    def list_all(self) -> list[type[Problem]]:
        return self.session.query(Problem).all()

    def add(self, problem: Problem) -> None:
        self.session.add(problem)
        self.session.commit()




