# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 17:41:31 2020

@author: Admin
"""

import tensorflow as tf
tf.compat.v1.disable_v2_behavior()
print("version:",tf.version.VERSION)


#declare two symbolic floating-point scalars

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

#creating simple symbolic expression 

add = tf.add(a, b)
sess = tf.Session()

#binding 1.5 to 'a' and 2.5 to 'b' and evaluating 'c'
binding = {a: 1.5, b: 2.5}
c = sess.run(add, feed_dict=binding)
print(c)
print(tf.version.VERSION)