import logging

from os import environ
from numpy import ndarray
from urllib.parse import urljoin

from app.classifier import ImageClassifier


class ClassifierService:
    """Classifier Service

    """

    _logger = logging.getLogger(__name__)
    _instance = None
    classifier = None


    def _init_feature_extractor(self) -> None:
        tf_serving_url = environ['TF_SERVING_URL']
        tf_model_name = environ['TF_SERVING_MODEL_NAME']
        tf_path_name = environ['TF_SERVING_MODEL_PATH']
        se_url = environ['QDRANT_URL']
        se_port = environ['QDRANT_PORT']
        collection_name = environ['QDRANT_COLLECTION_NAME']

        tf_serving_model_url = '/'.join(s.strip('/') for s in [
            tf_serving_url,
            tf_path_name,
            tf_model_name]
        )

        self.classifier = ImageClassifier(
            tf_serving_model_url,
            qdrant_url=se_url,
            qdrant_port=se_port,
            collection_name=collection_name
        )

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._logger.info(f'Create {cls.__name__}')
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._init_feature_extractor()
        return cls._instance

    def predict(self, image: ndarray):
        if not isinstance(image, ndarray): raise Exception
        return self.classifier.predict(image)
