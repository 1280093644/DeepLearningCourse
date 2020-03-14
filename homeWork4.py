import numpy as np
x0 = np.ones(10)
x1 = np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
x2 = [2,3,4,2,3,4,2,4,1,3]
y = np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])
x = np.stack((x0,x1,x2),axis = 1)
print('X堆叠效果如下：')
print(x)
y2 = y.reshape(10,1)
print('Y堆叠效果如下：')
print(y2)
m1 = np.mat(x)
m2 = np.mat(y2)
w = (1/(m1.T*m1))*m1.T*m2
print("w的形状为：")
print(np.shape(w))
print("w的值为：")
print(w)
