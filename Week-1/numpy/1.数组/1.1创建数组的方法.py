# -*- codeing = utf-8 -*-
# @Time : 2024/4/16 20:18
# @Author : Li Wenhai
# @Software : PyCharm
import numpy as np

a = np.array([1,2,3,4,5])
b = np.array(range(1,6))
c = np.arange(1,6)
d = np.array(range(1,8),dtype=float)

print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)
print('*'*50)

e = np.zeros(10)
f = np.zeros((2,4))

g = np.full(3,520)
h = np.full((2,4),520)

print(g)
print(f)