import tensorflow as tf
from tensorflow.keras.layers import Layer


class ArcFaceBlock(Layer):
    """
    Keras implementation of https://arxiv.org/abs/1801.07698
    For more information about code refers to :
    https://keras.io/guides/making_new_layers_and_models_via_subclassing/
    Code was inspired by :
    https://github.com/4uiiurz1/keras-arcface
    """

    def __init__(self, n_classes, **kwargs):
        super(ArcFaceBlock, self).__init__(**kwargs)
        self.n_classes = n_classes
        self.W = None

    def build(self, input_shape):
        super(ArcFaceBlock, self).build(input_shape)

        self.W = self.add_weight(
            name='w',
            shape=(input_shape[-1], self.n_classes),
            initializer='random_normal',
            trainable=True,
        )

    def call(self, inputs, **kwargs):
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
