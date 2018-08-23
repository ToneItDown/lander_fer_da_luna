import tensorflow as tf
cost = tf.constant(5, dtype=tf.float32)
addone = cost+1
print (addone)

with tf. Session () as sess:
    print(sess.run(addone))
    