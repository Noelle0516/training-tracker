import uuid
from datetime import datetime

from db.session import Base
from sqlalchemy import Column, DateTime, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

class TrainingLogs(Base):
    __tablename__ = 'traininglogs'
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    emp_name = Column(Text)
    emp_id = Column(Integer)
    completion_date = Column(DateTime, default=datetime.now())
    trainer_id = Column(Integer)
    category = Column(Text)
    description = Column(Text)
    name = Column(Text)
    expiry_period = Column(Integer, default=0)