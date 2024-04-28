# -*- codeing = utf-8 -*-
# @Time : 2024/4/21 21:05
# @Author : Li Wenhai
# @Software : PyCharm
import numpy as np
一维 = np.random.random(3)
print(f'生成3个0.0至1.0的随机数:\n{一维}')
二维 = np.random.random(size=(2,3))
print(f'生成2行3列共6个数的0.0至1.0的随机数:\n{二维}')
三维 = np.random.random(size=(3,2,3))
print(f'生成三块2行3列，每块6个数的0.0至1.0的随机数:\n{三维}')