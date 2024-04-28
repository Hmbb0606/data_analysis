# -*- codeing = utf-8 -*-
# @Time : 2024/4/21 21:43
# @Author : Li Wenhai
# @Software : PyCharm

# 一维数组：
import numpy as np
a = np.array([3,6,7,9,2,1,8,5,4])
a.sort()
print(a)

# 二维数组：
a = np.array([[0,12,48],[4,18,14],[7,1,99]])
print(f'数组：\n{a}')
print('-'*30)
print(np.sort(a))  # 默认按最后的轴排序，就是（行，列）（0，1）
print('-'*30)
print(np.sort(a,axis=0))  # 按行排序