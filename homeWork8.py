import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = "SimHei"
mnist = tf.keras.datasets.mnist
(train_x,train_y),(test_x,test_y) = mnist.load_data()
plt.figure(figsize=(12,12))
for i in np.arange(16):
    num = np.random.randint(1,10000)
    plt.subplot(4,4,(i+1))
    plt.axis("off")
    plt.imshow(test_x[num],cmap="gray")
    plt.title("标签值："+str(test_y[num]),fontsize = 14)
plt.suptitle("MNIST测试集样本",fontsize=20,color ="red")
plt.show()
