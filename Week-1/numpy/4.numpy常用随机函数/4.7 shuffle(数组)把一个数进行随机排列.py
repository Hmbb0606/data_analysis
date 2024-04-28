# -*- codeing = utf-8 -*-
# @Time : 2024/4/21 21:08
# @Author : Li Wenhai
# @Software : PyCharm
import numpy as np
一维数组 = np.arange(10)
print(f'没有随机排列前的一维数组{一维数组}')
np.random.shuffle(一维数组)
print(f'随机排列后的一维数组{一维数组}')

二维数组 = np.arange(20).reshape(4,5)
print(f'没有随机排列前的二维数组\n{二维数组}\n')
np.random.shuffle(二维数组)
print(f'随机排列后的二维数组\n{二维数组}')

三维数组 = np.arange(12).reshape(2,2,3)
print(f'没有随机排列前的三维数组\n{三维数组}\n')
np.random.shuffle(三维数组)
print(f'随机排列后的三维数组\n{三维数组}')