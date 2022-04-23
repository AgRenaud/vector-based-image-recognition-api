import logging

from fastapi import APIRouter, File, UploadFile

from app.service_layer import handlers


router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/classifier/predict")
async def predict_class(image_file: UploadFile = File(...)):
    img = await image_file.read()

    return handlers.get_img_class(img)


