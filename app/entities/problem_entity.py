from datetime import datetime
from sqlalchemy.orm.attributes import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Enum, Integer, DateTime, Date

from app.entities.Base_entity import Base
from app.domain.difficulty_level import DifficultyLevel


class Problem(Base):
    __tablename__ = 'problems'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    difficulty: Mapped[DifficultyLevel] = mapped_column(Enum(DifficultyLevel), nullable=False)
    created_on: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(), nullable=False)
    updated_on: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now(), nullable=False)

    def __init__(self, title: str, difficulty: DifficultyLevel):
        super().__init__()  # Got to look at why is this needed?
        self.title = title
        self.difficulty = difficulty

    def __repr__(self) -> str:
        return f"Problem(id:{self.id}, title={self.title}, difficulty={self.difficulty})"