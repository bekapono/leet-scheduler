from app.repository.scheduler_repository import SchedulerRepository


class SchedulerService:
    def __init__(self, repository: SchedulerRepository) -> None:
        self.repository = repository

    def due_today(self) -> list[str]:
        pass