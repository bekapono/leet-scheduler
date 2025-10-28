from app.repository.scheduler_repository import SchedulerRepository
from app.dto.scheduler_dto import SchedulerRequestDTO, SchedulerResponseDTO
from app.entities.scheduler_entity import Schedule


class SchedulerService:
    def __init__(self, repository: SchedulerRepository) -> None:
        self.repository = repository

    async def create_scheduler(self, request: SchedulerRequestDTO) -> SchedulerResponseDTO:
        pass

    def map_to_new_scheduler(self, request: SchedulerRequestDTO) -> Schedule:
        pass

    def map_to_response_dto(self, schedule: Schedule) -> SchedulerResponseDTO:
        pass

    def due_today(self) -> list[str]:
        pass

