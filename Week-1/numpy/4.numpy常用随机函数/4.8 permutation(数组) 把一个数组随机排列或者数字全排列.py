# -*- codeing = utf-8 -*-
# @Time : 2024/4/21 21:13
# @Author : Li Wenhai
# @Software : PyCharm
import numpy as np
# 与上面讲的np.random.shuffle(一维数组)效果一样,就是把一维数组重新排序了
排列 = np.random.permutation(10)    # 这里的10就看成是range(10)
print(排列)

二维数组 = np.arange(9).reshape((3,3))
print(f'没有随机排列前的二维数组是\n{二维数组}\n')
排序后 = np.random.permutation(二维数组)
print(f'随机排列后的二维数组是\n{排序后}\n')