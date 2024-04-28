# -*- codeing = utf-8 -*-
# @Time : 2024/4/16 20:06
# @Author : Li Wenhai
# @Software : PyCharm

import numpy as np

#列表推导公式
# [变量名 for 变量名 in range(1,n+1)]
def array_add(n):
    n = 3
    a = [i**3 for i in range(1,n+1)]
    b = [i**2 for i in range(1,n+1)]
    c = []
    for i in range(n):
        c.append(a[i]+b[i])
    return c

def numpy_add(n):
    a = np.arange(1, n+1) ** 3
    b = np.arange(1, n+1) ** 2
    return a+b

#python是先循环再计算，numpy直接计算，计算数量越大越节约时间
print(array_add(3))
print(numpy_add(3))