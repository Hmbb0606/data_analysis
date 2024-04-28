# -*- codeing = utf-8 -*-
# @Time : 2024/4/21 21:30
# @Author : Li Wenhai
# @Software : PyCharm
# 沿轴向进行计算，一维数组只有一个0轴
import numpy as np
a = np.array([1,2,3,4,3,5,3,6,6])
print(f'数组：{a}')
print(np.sum(a))
print(np.prod(a)) #垒乘
print(np.cumsum(a))   # 从0开始元素的累积和
print(np.cumprod(a))  # 从1开始元素的累积积
print(np.max(a))
print(np.min(a))
print(np.argmax(a))    # 最大值所在的下标
print(np.argmin(a))    # 最小值所在的下标
print(np.mean(a))      # 平均数
print(np.median(a))    # 中位数
print(np.average(a))   # 加权平均
counts = np.bincount(a) # 统计非负整数的个数，不能统计浮点数
print(np.argmax(counts)) # 返回众数,此方法不能用于二维数组

# Numpy中没有直接的方法求众数，但是可以这样实现：
# bincount（）：统计非负整数的个数，不能统计浮点数
# counts = np.bincount(a)
# #返回众数
# np.argmax(counts)