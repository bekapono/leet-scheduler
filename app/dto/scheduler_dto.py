from pydantic import BaseModel


class SchedulerRequestDTO(BaseModel):
    id: int

class SchedulerResponseDTO(BaseModel):
    problem_id: int
    dates: list[str]