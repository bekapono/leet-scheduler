from sqlalchemy.engine.create import create_engine
from sqlalchemy.orm.session import sessionmaker

from app.entities.Base_entity import Base
from app.repository.problem_repository import ProblemRepository
from app.repository.scheduler_repository import SchedulerRepository
from app.services.problem_service import ProblemService
from app.services.scheduler_service import SchedulerService


def test_session():
    engine = create_engine('sqlite:///test.db', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


class ProblemServiceDependency:
    def __init__(self):
        self.repository = ProblemRepository(test_session())
        self.problem_service = ProblemService(self.repository)


def problem_service_factory() -> ProblemService:
    dependency = ProblemServiceDependency()
    return dependency.problem_service


class SchedulerServiceDependency:
    def __init__(self):
        self.repository = SchedulerRepository(test_session())
        self.scheduler_service = SchedulerService(self.repository)


def scheduler_service_factory() -> SchedulerService:
    dependency = SchedulerServiceDependency()
    return dependency.scheduler_service

