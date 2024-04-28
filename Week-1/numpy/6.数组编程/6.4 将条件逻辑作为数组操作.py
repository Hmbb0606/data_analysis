# -*- codeing = utf-8 -*-
# @Time : 2024/4/21 21:40
# @Author : Li Wenhai
# @Software : PyCharm
import numpy as np
a = np.array([[1,3,6],[9,3,2],[1,4,3]])
print(f'数组:\n{a}')
print('-'*30)
print(a > 3)
print('-'*30)
print(np.where(a>3,520,1314))