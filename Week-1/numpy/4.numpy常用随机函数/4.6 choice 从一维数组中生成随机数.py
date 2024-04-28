# -*- codeing = utf-8 -*-
# @Time : 2024/4/21 21:06
# @Author : Li Wenhai
# @Software : PyCharm
import numpy as np
# 第一参数是一个1维数组，如果只有一个数字那就看成range(5)
# 第二参数是维度和元素个数，一个数字是1维，数字是几就是几个元素
a = np.random.choice(5,5)
print(f'从range(5)中拿随机数，生成只有5个元素的一维数组是：{a}')

b = np.random.choice(5,(2,3))
print(f'从range(5)中拿随机数，生成2行3列的数组是：\n{b}')

c = np.random.choice([1,2,9,4,8,6,7,5],3)
print(f'从[1,2,9,4,8,6,7,5]数组中拿随机数，3个元素：{c}')

d = np.random.choice([1,2,9,4,8,6,7,5],(2,3))
print(f'从[1,2,9,4,8,6,7,5]数组中拿随机数，生成2行3列的数组是：\n{d}')