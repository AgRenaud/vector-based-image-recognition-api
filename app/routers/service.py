import logging

import numpy as np
import cv2

from fastapi import APIRouter, File, UploadFile

from app.schemas import Input
from app.service import ClassifierService


router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/classifier/predict")
async def predict_class(image_file: UploadFile = File(...)):
    img = await image_file.read()
    nparr = np.fromstring(img, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return ClassifierService().predict(img_np)
