from datetime import datetime
from sqlalchemy.orm.attributes import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Enum, Integer, DateTime, Date
from app.entities.Base_entity import Base


class Schedule(Base):
    __tablename__ = 'schedule'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    problem_id: Mapped[int] = mapped_column(Interger, foreign_key='problem_id')
    scheduled_on: Mapped[date] = mapped_column(Date, nullable=False)
    interval_day: Mapped[int] = mapped_column(Integer, nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self) -> str:
        return (f"Schedule(id:{self.id}, problem_id:{self.problem_id}, interval_day:{self.interval_day},"/
                f" scheduled_on:{self.scheduled_on}, completed:{self.completed})")

