# -*- codeing = utf-8 -*-
# @Time : 2024/4/21 21:44
# @Author : Li Wenhai
# @Software : PyCharm
import numpy as np
x = np.array([59, 29, 39])
a = np.argsort(x)
print(f'索引升序：{a}')  # 升序
# argsort函数返回的是数组值从小到大的索引值,[3, 1, 2]从小到大为[1，2，3],期对应的索引为[1，2，0]
print(f'数组升序：{x[a]}')  # 以排序后的顺序重构原数组
b = np.argsort(-x)  # 降序
print(f'索引降序：{b}')
print(f'数组升序：{x[b]}')

import numpy as np
x = np.array([[0, 12, 48], [4, 18, 14], [7, 1, 99]])
a1 = np.argsort(x)
print(f'索引排序：\n{a1}')
print('-'*30)
# 以排序后的顺序重构原数组，注意与一维数组的形式不一样
print(np.array([np.take(x[i], x[i].argsort()) for i in range(3)]))