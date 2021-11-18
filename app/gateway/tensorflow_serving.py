import json
import requests

from numpy import array


class TensorflowServingGateway:
    """
    Example:
        import numpy as np

        img = np.random.rand(28,28,1)

        url = "http://localhost:8501/v1/models/my_production_model"
        tf = TensorflowServingGateway(tf_serving_url=url)

        tf.infer(img)
    """


    def __init__(self, tf_serving__model_url : str):
        self.tf_serving__model_url = tf_serving__model_url

    def infer(self, img: array):
        headers = {
            'Content-type': 'application/json'
        }
        
        body = {
            "signature_name": "serving_default",
            "instances": [img.tolist()]
        }

        data = json.dumps(body)
        req = requests.post(self.tf_serving__model_url + ':predict', data=data, headers=headers)
        res = req.json()

        return res
