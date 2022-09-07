from typing import Generator

from db.session import SessionLocal
from google.cloud.pubsub import PublisherClient

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_publisher() -> PublisherClient:
    with PublisherClient() as client:
        yield client
