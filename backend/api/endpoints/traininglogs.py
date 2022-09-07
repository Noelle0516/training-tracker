import os
from asyncore import write
from datetime import datetime, timezone
from functools import lru_cache
from typing import List, Optional

from api import deps
from fastapi import APIRouter, Depends
from google.cloud.pubsub import PublisherClient
from models.traininglogs import TrainingLogs
from schemas.traininglogs import TrainingLogsSchema
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/addnewtraininglog", response_model=str)
def add_new_training_event(
    event: TrainingLogsSchema,
    db: Session = Depends(deps.get_db),
    publisher: PublisherClient = Depends(deps.get_publisher),
):
    return "OK"