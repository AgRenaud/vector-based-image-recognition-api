import logging

from fastapi import APIRouter, WebSocket

from app.service_layer import handlers


router = APIRouter()

logger = logging.getLogger(__name__)


@router.websocket("/")
async def streaming_predict_class(websocket: WebSocket):

    await websocket.accept()

    while True:
        data = websocket.receive_bytes()
        img = ... # Transform bytes into img
        result =  handlers.get_img_class(img)
        await websocket.send_json({})
