import cv2
import logging

import numpy as np

from app.adapters import api


class ImageClassifier:

    _logger = logging.getLogger(__name__)

    def __init__(
        self,
        features_extractor: api.TensorflowServingGateway,
        classifier: api.QdrantGateway,
    ):
        self.features_extractor = features_extractor
        self.classifier = classifier

    def predict(self, image: np.ndarray):
        prep_img = self._get_image_preprocessing(image)
        features = self._get_features(prep_img).get("predictions")[0]
        pred_class = self._get_class(features)
        return pred_class

    def _get_image_preprocessing(self, image: np.ndarray):
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if img.shape[:2] != (28, 28):
            img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_CUBIC)
        img = img[:, :, np.newaxis].astype("float32") / 255

        return img

    def _get_features(self, image: np.ndarray):
        return self.features_extractor.predict(image)

    def _get_class(self, features_vector: np.ndarray):
        search_result = self.classifier.search(features_vector)
        best_match = sorted(search_result, key=lambda d: d["score"], reverse=True)[0]
        return best_match
