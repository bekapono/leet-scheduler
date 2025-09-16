from fastapi import APIRouter, Depends

from app.dto.problems_dto import ProblemRequestDTO
from app.services.problem_service import ProblemService

router = APIRouter()


@router.post("/problems")
async def create_problems(dto: ProblemRequestDTO, problem_service: Depends(ProblemService)):
    return await problem_service.create_problems(dto)
