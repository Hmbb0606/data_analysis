# -*- codeing = utf-8 -*-
# @Time : 2024/4/21 21:21
# @Author : Li Wenhai
# @Software : PyCharm
import numpy as np
a = np.random.uniform(1,10,10)
print(f'在1到10之间生成10个随机数：\n{a}')

b = np.random.uniform(1,10,(2,3))
print(f'在1到10之间生成2行3列共计6个随机数：\n{b}')