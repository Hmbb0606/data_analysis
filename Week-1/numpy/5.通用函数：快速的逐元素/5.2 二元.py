# -*- codeing = utf-8 -*-
# @Time : 2024/4/21 21:24
# @Author : Li Wenhai
# @Software : PyCharm
import numpy as np
x = np.random.randn(8)
y = np.random.randn(8)
print(x)
print('--------')
print(y)
print('--------')
print(np.maximum(x,y))
# 对位比较大小，取大的，生成新的数组返回，逐个元素地将 x和 y 中元素的最大值计算出来