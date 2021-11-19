from os import environ
from urllib.parse import urljoin

from app.classifier import ImageClassifier


class ClassifierService:
    """Classifier Service

    """

    _instance = None

    classifier = None


    def _init_classifier(self) -> None:
        tf_serving_url = environ['TF_SERVING_URL']
        tf_model_name = environ['TF_SERVING_MODEL_NAME']
        tf_path_name = environ['TF_SERVING_MODEL_PATH']
        tf_serving_model_url = '/'.join(s.strip('/') for s in [
            tf_serving_url,
            tf_path_name,
            tf_model_name]
        )
        self.classifier = ImageClassifier(tf_serving_model_url)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._init_classifier()
        return cls._instance

    def predict(self, image):
        return self.classifier.predict(image)
