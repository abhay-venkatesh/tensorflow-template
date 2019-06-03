import tensorflow as tf
import tensorflow.contrib.eager as tfe

if __name__ == "__main__":
    tfe.enable_eager_execution()
    a = tf.constant(2)
    print(a)