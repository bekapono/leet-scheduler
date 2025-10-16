from fastapi import APIRouter, Depends
from typing import Annotated

from app.dependencies import problem_service_factory
from app.dto.problems_dto import ProblemRequestDTO
from app.dto.scheduler_dto import SchedulerRequestDTO
from app.services.problem_service import ProblemService, NewProblemResponseDTO
from app.services.scheduler_service import SchedulerService

router = APIRouter()


@router.post("/problems")
async def create_problems(
        dto: ProblemRequestDTO,
        problem_service: Annotated[ProblemService, Depends(problem_service_factory)],
        scheduler_service: Annotated[SchedulerService, Depends(SchedulerService)]
    ) -> NewProblemResponseDTO:
    # return await problem_service.create_problem(dto)
    problem = await problem_service.create_problem(dto)
    schedule = await scheduler_service.create_scheduler(SchedulerRequestDTO(id=problem.id))
    return NewProblemResponseDTO(**problem.model_dump(), dates=schedule.dates)
