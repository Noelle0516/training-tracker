from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

from api.api import api_router
from db.session import Base, engine


try:
    print("initializing db")
    Base.metadata.create_all(engine)
    print("db initialized")
except:
    print("failed to initialize DB")


def create_app() -> FastAPI:
    application = FastAPI()
    application.include_router(api_router)

    for route in application.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name

    return application


app = create_app()
