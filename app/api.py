import sys
import logging
from fastapi import FastAPI

from config import get_app_config
from routers import health


get_app_config()

logger = logging.getLogger(__name__)

def create_app():
    app = FastAPI()

    app.include_router(health.router, prefix='/health')

    return app
