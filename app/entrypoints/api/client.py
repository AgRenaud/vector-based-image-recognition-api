import sys
import logging
from fastapi import FastAPI

from app.config import get_app_config
from app.entrypoints.api import v1


get_app_config()

logger = logging.getLogger(__name__)


def create_app():

    app = FastAPI()

    app.include_router(v1.router, prefix="/api/v1")

    return app
