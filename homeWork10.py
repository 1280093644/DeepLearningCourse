import tensorflow as tf
import numpy as np
x = tf.constant([ 64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y = tf.constant([ 62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])
sum1 = 10*tf.reduce_sum(x*y)
sum2 = tf.reduce_sum(x)*tf.reduce_sum(y)
sum3 =10*tf.reduce_sum(x**2)
sum4 = (tf.reduce_sum(x))**2
w = (sum1-sum2)/(sum3-sum4)
b = (tf.reduce_sum(y)-w*tf.reduce_sum(x))/10
print("w的值为：",w)
print("b的值为：",b)
