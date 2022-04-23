import sys
import logging
from fastapi import FastAPI

from app import config
from app.entrypoints.api import v1


def create_app():
    
    config.set_loggers()

    logger = logging.getLogger(__name__)

    app = FastAPI()
    app.include_router(v1.router, prefix="/api/v1")

    return app
