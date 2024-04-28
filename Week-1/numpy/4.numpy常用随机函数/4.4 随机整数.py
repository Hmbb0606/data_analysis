# -*- codeing = utf-8 -*-
# @Time : 2024/4/21 21:04
# @Author : Li Wenhai
# @Software : PyCharm
import numpy as np
a = np.random.randint(3)
print(f'随机0至3之间的整数是：{a}')
b = np.random.randint(1,10)
print(f'随机1至10之间的整数是：{b}')
c = np.random.randint(1,10,size=(5,))
print(f'随机1至10之间取5个元素组成一维数组{c}')
d = np.random.randint(1,20,size=(3,4))
print(f'随机1至20之间取12个元素组成二维数组：\n{d}')
e = np.random.randint(1,20,size=(2,3,4))
print(f'随机1至20之间取24个元素组成三维数组：\n{e}')