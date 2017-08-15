'''
Created on 2017. 6. 24.

@author: Summit
'''

import tensorflow as tf

a = tf.placeholder("float")
b = tf.placeholder("float")

y = tf.multiply(a,b)

sess = tf.Session()

print(sess.run(y, feed_dict={a:3, b:3}))