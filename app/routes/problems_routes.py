from fastapi import APIRouter, Depends
from typing import Annotated

from app.dependencies import problem_service_factory
from app.dto.problems_dto import ProblemRequestDTO
from app.services.problem_service import ProblemService, ProblemResponseDTO
from app.services.scheduler_service import SchedulerService

router = APIRouter()


@router.post("/problems")
async def create_problems(
        dto: ProblemRequestDTO,
        problem_service: Annotated[ProblemService, Depends(problem_service_factory)],
        scheduler_service: Annotated[SchedulerService, Depends(SchedulerService)]
    ) -> ProblemResponseDTO:
    # return await problem_service.create_problem(dto)
    pass
