# -*- codeing = utf-8 -*-
# @Time : 2024/4/21 19:44
# @Author : Li Wenhai
# @Software : PyCharm
import numpy as np
import random
a = np.arange(10).reshape(2,5)
b = np.random.randn(2,5)
print(a+b)
print(a-b)

print('*'*50)

a = np.arange(6)
b = np.arange(24).reshape(4,6)
print(a)
print(b)
print(b-a)

# 总结：
# （1）形状一样的数组按对应位置进行计算。
# （2）一维和多维数组是可以计算的，只要它们在某一维度上是一样的形状，仍然是按位置计算。