import os
import unittest

import numpy as np

from unittest import mock
from unittest.mock import MagicMock

from app.service import ClassifierService
from app.classifier import ImageClassifier


class TestClassifierService(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.env_patcher = mock.patch.dict(
            os.environ,
            {"TF_SERVING_URL": "tf_serving_url",
             "TF_SERVING_MODEL_NAME": "tf_serving_model_name",
             "TF_SERVING_MODEL_PATH": "tf_serving_model_path",
             "QDRANT_URL": "qdrant_url",
             "QDRANT_PORT": "qdrant_port",
             "QDRANT_COLLECTION_NAME": "qdrant_collection_name"})
        cls.env_patcher.start()

        super().setUpClass()

    @mock.patch('app.classifier.ImageClassifier')
    def test_predict_class(self, image_classifier):
        service = ClassifierService()
        image_classifier.predict.return_value = {"class": "h", "score": 0.96093374}
        service.classifier = image_classifier
        x = np.random.rand(28,28)
        self.assertEqual({"class": "h", "score": 0.96093374}, service.predict(x))
        self.assertRaises(Exception, service.predict, 4)
