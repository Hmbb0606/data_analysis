# -*- codeing = utf-8 -*-
# @Time : 2024/4/17 16:15
# @Author : Li Wenhai
# @Software : PyCharm

import numpy as np
a = np.array(range(1,8),dtype=float)       # 修改数据类型
b = np.array(range(1,8),dtype='float32') # 修改数据类型和位数
print(a)
print(b)
print(a.dtype)
print(b.dtype)
print(type(a))
print(type(b))