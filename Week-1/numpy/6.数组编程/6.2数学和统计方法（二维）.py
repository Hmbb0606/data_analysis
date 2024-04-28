# -*- codeing = utf-8 -*-
# @Time : 2024/4/21 21:33
# @Author : Li Wenhai
# @Software : PyCharm
import numpy as np
# from scipy import stats
a = np.array([[1,3,6],[9,2,3],[2,3,3]])
print(f'数组：\n{a}')
print('-'*30)
print(np.sum(a))
print(np.prod(a))
print(np.cumsum(a))    # 从0开始元素的累积和，返回一维数组
print(np.cumprod(a))   # 从1开始元素的累积积，返回一维数组
print(np.max(a))
print(np.min(a))
print(np.argmax(a))
print(np.argmin(a))
print(np.mean(a))
print(np.median(a))
print(np.average(a))