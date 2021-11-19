import logging

from numpy import array

from app.gateway import TensorflowServingGateway


class ImageClassifier:
    """
    An image classifier based on features extraction and nearest neighbor algorithm.

    Parameters
    ----------
    tf_serving_model_url : str
        The url to tensorflow serving model. It must contains the full path to the model.
        Example: http://my-host/full/path/my-model
    """

    _logger = logging.getLogger(__name__)

    def __init__(self, tf_serving_model_url: str):
        self.features_extractor = TensorflowServingGateway(tf_serving_model_url)

    def predict(self, image: array):
        prep_img = self.__get_image_preprocessing(image)
        features = self.__get_features(prep_img)
        return features

    def __get_image_preprocessing(self, image:array):
        return image

    def __get_features(self, image: array):
        return self.features_extractor.predict(image)

    def __get_class(self, features_vector: array):
        pass
