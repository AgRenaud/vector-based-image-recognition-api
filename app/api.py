import sys
import logging
from fastapi import FastAPI

from app.config import get_app_config
from app.routers import health, service


get_app_config()

logger = logging.getLogger(__name__)


def create_app():
    app = FastAPI()

    app.include_router(health.router, prefix="/health")
    app.include_router(service.router, prefix="/service")

    return app
