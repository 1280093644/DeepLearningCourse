import tensorflow as tf
import numpy as np
x = tf.constant([ 64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y = tf.constant([ 62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])
sumx = 0
sumy = 0
fz = 0
fm = 0
for i in np.arange(10):
    sumx+=x[i]
    sumy+=y[i]
avgsumx=sumx/10
avgsumy=sumy/10
fz = tf.reduce_sum((x-avgsumx)*(y-avgsumy))
fm = tf.reduce_sum((x-avgsumx)**2)
w = fz/fm
b = avgsumy-w*avgsumx
print("W的值为：",w)
print("b的值为：",b)
