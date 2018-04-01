import tensorflow as tf

hello = tf.constant('Hola, Tensor Flow!')

sess = tf.Session()

print(sess.run(hello))
