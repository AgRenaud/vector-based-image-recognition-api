import json
import requests
import logging

from numpy import array


class TensorflowServingGateway:
    """
    Example:
        import numpy as np

        img = np.random.rand(28,28,1)

        url = "http://localhost:8501/v1/models/my_production_model"
        tf = TensorflowServingGateway(tf_serving_model_url=url)

        tf.predict(img)
    """

    _logger = logging.getLogger(__name__)

    def __init__(self, tf_serving_model_url : str):
        self.tf_serving_model_url = tf_serving_model_url

    def predict(self, img: array):
        headers = {
            'Content-type': 'application/json'
        }

        body = {
            "signature_name": "serving_default",
            "instances": [img.tolist()]
        }

        data = json.dumps(body)
        req = requests.post(self.tf_serving_model_url + ':predict', data=data, headers=headers)
        res = req.json()

        return res
