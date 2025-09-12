from datetime import datetime
from sqlalchemy.orm.attributes import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Enum, Integer, DateTime, Date

from Base_entity import Base


class ProblemEntity(Base):
    __tablename__ = 'problems'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    difficulty: Mapped[Enum] = mapped_column(
        Enum("EASY", "MEDIUM", "HARD", name="difficulty_level"),
        nullable=False
    )
    created_on: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(), nullable=False)
    updated_on: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now(), nullable=False)

    def __repr__(self) -> str:
        return f"ProblemEntity(id:{self.id}, title={self.title}, difficulty={self.difficulty})"