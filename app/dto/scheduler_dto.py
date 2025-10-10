from pydantic import BaseModel


class SchedulerRequestDTO(BaseModel):
    problem_id: int

class SchedulerResponseDTO(BaseModel):
    problem_id: int
    scheduled_list: list[str]