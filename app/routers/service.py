import logging

from fastapi import APIRouter

from app.schemas import Input
from app.service import ClassifierService


router = APIRouter()

logger = logging.getLogger(__name__)

@router.get('/classifier/predict')
def compute_single_vector(input: Input):
    img = input.values
    return ClassifierService().predict(img)
