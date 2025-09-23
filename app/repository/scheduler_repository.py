from datetime import date
from sqlalchemy.orm import Session


class SchedulerRepository:
    def __init__(self, session: Session | None) -> None:
        self.session = session

    def list_all_problems_due_today(self, today_date: date) -> list[str]:
        """ 
            this method needs to:
            1. get the list of problem_ids from scheduler by date
            2. get the list of titles from problems by the problems_id provided
               by scheduler
               
            still deciding on return actual back to service? or a snapshot of results
        """
        pass