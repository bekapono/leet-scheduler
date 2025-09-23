from sqlalchemy.engine.create import create_engine
from sqlalchemy.orm.session import sessionmaker

from app.entities.Base_entity import Base
from app.repository.problem_repository import ProblemRepository
from app.services.problem_service import ProblemService


class ProblemServiceDependency:
    def __init__(self):
        self.repository = ProblemRepository(self.test_session())
        self.problem_service = ProblemService(self.repository)

    @staticmethod
    def test_session():
        engine = create_engine('sqlite:///test.db', echo=False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session


def problem_service_factory() -> ProblemService:
    dependency = ProblemServiceDependency()
    return dependency.problem_service

