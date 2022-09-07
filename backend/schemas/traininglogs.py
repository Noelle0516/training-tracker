from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

class TrainingLogsSchema(BaseModel):
    class Config:
        orm_mode = True

    id: Optional[UUID]
    emp_name: str
    emp_id: int
    completion_date: datetime
    trainer_id: int
    category: str
    description: Optional[str]
    name: str
    expiry_period: int