import logging
from fastapi import APIRouter


router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/")
def health():
    logger.info("check health")
    return {"api": {"is_up": True}}
