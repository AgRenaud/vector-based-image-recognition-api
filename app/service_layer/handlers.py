import cv2
import logging

import numpy as np

from app import config
from app.adapters import api
from app.service_layer.image_classifier import ImageClassifier


logger = logging.getLogger(__name__)


def get_img_class(img: np.ndarray):

    classifier = ImageClassifier(
        api.TensorflowServingGateway(config.get_tf_serving_credentials()),
        api.QdrantGateway(*config.get_qdrant_credentials(), "CharactersVectors"),
    )

    im = np.fromstring(img, np.uint8)
    im = cv2.imdecode(im, cv2.IMREAD_COLOR)

    logger.info(f"received image of shape : {im.shape}")

    return classifier.predict(im)
