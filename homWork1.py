import math
a = float(input("请输入a的值：a="))
b = float(input("请输入b的值：b="))
c = float(input("请输入c的值：c="))
deta = b**2-4*a*c
if a!=0:
    if deta > 0:
        s1 = (-b+math.sqrt(deta))/(2*a)
        s2 = (-b-math.sqrt(deta))/(2*a)
        print("该一元二次方程有两个不同的解：")
        print("s1=:",s1)
        print("s2=:",s2)
    if deta == 0:
        s1 = (-b+math.sqrt(deta))/(2*a)
        print("该一元二次方程有两个相同的解:")
        print("s1=s2=:",s1)
    if deta < 0:
        print("该一元二次方程无解！")
else:
    s=-c/b
    print("此方程为一元一次方程")
    print("该一元一次方程的解为：")
    print("s=:",s)
