from fastapi import APIRouter, Depends
from typing import Annotated

from app.dto.problems_dto import ProblemRequestDTO
from app.services.problem_service import ProblemService, ProblemResponseDTO

router = APIRouter()


@router.post("/problems")
async def create_problems(dto: ProblemRequestDTO, problem_service: Annotated[ProblemService, Depends(ProblemService)]) -> ProblemResponseDTO:
    return await problem_service.create_problem(dto)
