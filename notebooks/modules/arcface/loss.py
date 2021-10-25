import tensorflow as tf
import tensorflow.keras.backend as K
from tensorflow.keras.losses import CategoricalCrossentropy


def arcface_loss(m, s):

    def compute_loss(y_true, y_pred):
        theta = tf.math.acos(K.clip(y_pred, -1.0 + K.epsilon(), 1.0 - K.epsilon()), name='arccos')
        thetaM = tf.math.add(theta, m, name='add_margin')
        marginal_target_logit = tf.cos(thetaM, name='marginal_logit')
        a = tf.math.multiply((1 - y_true), y_pred, name='gt_logits')
        b = tf.math.multiply(marginal_target_logit, y_true, name='gt_marginal_logits')
        logit = tf.math.add(a, b, name='logit')
        scaled = tf.math.multiply(logit, s, name='scaled')
        softmax = tf.nn.softmax(scaled, name='softmax')
        loss_fn = CategoricalCrossentropy()
        loss = loss_fn(y_true, softmax)

        return loss

    return compute_loss
