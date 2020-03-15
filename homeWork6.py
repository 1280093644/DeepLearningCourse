import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = "SimHei"
plt.rcParams['axes.unicode_minus'] = False

boston_housing = tf.keras.datasets.boston_housing
(train_x,train_y),(test_x,test_y) = boston_housing.load_data(test_split = 0)
titles = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT']
plt.figure(figsize=(12,12))
for i in np.arange(13):
    plt.subplot(4,4,(i+1))
    plt.scatter(train_x[:,i],train_y)
    plt.xlabel(titles[i])
    plt.ylabel("Price($1000's)")
    plt.title(str(i+1)+"."+titles[i]+"-Price")
    plt.tight_layout()
    plt.suptitle("各个属性与房价的关系",x=0.5,y=1.02,fontsize=20)
plt.show()
for j in np.arange(13):
    print(str(j+1)+'--'+titles[j])
a = int(input('请选择属性：'))
for z in np.arange(1,14):
    if(a==z):
         plt.scatter(train_x[:,z-1],train_y)
         plt.xlabel(titles[z-1])
         plt.ylabel("Price($1000's)")
         plt.title(str(z)+"."+titles[z-1]+"-Price")
         plt.tight_layout()
plt.show()



