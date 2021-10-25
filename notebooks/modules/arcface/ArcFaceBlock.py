import tensorflow as tf
from tensorflow.keras.layers import Layer


class ArcFaceBlock(Layer):
    """
    Keras implementation of https://arxiv.org/abs/1801.07698
    Subclass of Layer
    INPUT x, y
        x : features vector
        y : Groundtruth one-hot matrix
    OUTPUT Softmax Layer
    The output of the layer is a Softmax for classification.
    For more information about code refers to :
    https://keras.io/guides/making_new_layers_and_models_via_subclassing/
    Code was inspired by :
    https://github.com/4uiiurz1/keras-arcface
    """

    def __init__(self, n_classes, **kwargs):
        """
        :param n_classes: number of classes
        :param s: scale parameter.
        :param m: margin parameter
        :param **kwargs: Additional keyword arguments.
        """
        super(ArcFaceBlock, self).__init__(**kwargs)
        self.n_classes = n_classes
        self.W = None

    def build(self, input_shape):
        """
        :param input_shape: the shape of the kernel. Length of the feature vector x by the number of classes.
        """
        super(ArcFaceBlock, self).build(input_shape)

        self.W = self.add_weight(
            name='w',
            shape=(input_shape[-1], self.n_classes),
            initializer='random_normal',
            trainable=True,
        )

    def call(self, inputs, **kwargs):
        """
        :param inputs: (x, y)
            x : features vector
            y : Groundtruth one-hot matrix
        :param **kwargs:
        :return: Softmax classification
        Implementation follows the algorithm shared in the paper special.
        """
        x = inputs
        x = tf.nn.l2_normalize(x, axis=0, name='X_Normalized')
        W = tf.nn.l2_normalize(self.W, axis=0, name='W_Normalized')
        W = tf.transpose(W)
        output = tf.linalg.matvec(W, x, name='Original_logit')
        return output

    def get_config(self):
        config = super().get_config().copy()
        config.update({
            'n_classes': self.n_classes,
        })
        return config
