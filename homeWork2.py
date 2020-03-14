import numpy.matlib
import numpy as np
arr1 = np.arange(1000)
np.random.seed(612)
result = np.random.uniform(0,1,1000)
a = int(input("请输入一个1-100之间的整数:"))
x = 1
for i in arr1:
    if i%a == 0:
        print(x,end="\t")
        print(i,end="\t")
        print(result[i])
        x = x+1
        