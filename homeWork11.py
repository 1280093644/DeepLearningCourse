import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['font.sans-serif'] = ['SimHei']
x1 = np.array([137.97,104.50,100.00,124.32,79.20,99.00,124.00,114.00,106.69,138.05,53.75,46.91,68.00,63.02,81.26,86.21])
x2 = np.array([3,2,2,3,1,2,3,2,2,3,1,1,1,1,2,2],dtype=np.float32)
y = np.array([145.00,110.00,93.00,116.00,65.32,104.00,118.00,91.00,62.00,133.00,51.00,45.00,78.50,69.65,75.69,95.30])
x0 = np.ones(len(x1))
X = tf.convert_to_tensor(np.stack((x0,x1,x2),axis = 1))
Y = tf.convert_to_tensor(y.reshape(-1,1))
Xt = tf.transpose(tf.convert_to_tensor(X))
W = tf.matmul(tf.matmul(tf.linalg.inv(tf.matmul(Xt,X)),Xt),Y)
W = np.array(W).reshape(-1)
areas = float(input("请输入商品房面积(20-500之间的实数)："))
rooms = int(input("请输入房间数(1-10之间的整数)："))
conareas = conrooms = 1
while conareas or conrooms:
    if areas<20 or areas>500:
        areas = float(input("请重新输入商品房面积(20-500)之间的实数："))
    else:
        conareas = 0
    if rooms<1 or rooms>10:
        rooms = int(input("请重新输入房间数(1-10之间的整数)："))
    else:
        conrooms = 0
y_pred = W[1]*areas+W[2]*rooms+W[0]
print("预测价格：",round(y_pred,2),"万元")




#X1,X2 = np.meshgrid(x1,x2)
#Y_PRED = W[0]+W[1]*X1+W[2]*X2
#fig = plt.figure()
#ax3d = Axes3D(fig)
#ax3d.scatter(x1,x2,y,color="b",marker="*",label="销售记录")
#ax3d.scatter(x1,x2,y_pred,color="r",label="预测房价")
#ax3d.plot_wireframe(X1,X2,Y_PRED,color="c",linewidth=0.5,label="拟合平面")

#ax3d.plot_surface(X1,X2,Y_PRED,cmap="coolwarm")
#ax3d.set_xlabel("Areas",color="r",fontsize=14)
#ax3d.set_ylabel("Rooms",color="r",fontsize=14)
#ax3d.set_zlabel("Price",color="r",fontsize=14)
#ax3d.set_yticks([1,2,3])
#plt.suptitle("商品房销售回归模型",fontsize=20)
#plt.legend(loc="upper left")
#plt.show()