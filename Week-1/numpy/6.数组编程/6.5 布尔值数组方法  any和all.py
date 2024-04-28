# -*- codeing = utf-8 -*-
# @Time : 2024/4/21 21:42
# @Author : Li Wenhai
# @Software : PyCharm
import numpy as np
a = np.array([[1,3,6],[9,3,2],[1,4,3]])
print(f'数组:\n{a}')
print('-'*30)
print((a>3).sum())  # 数组中大于3的数有多少个

# 对于布尔值数组，有两个常用方法any和all。
# any：检查数组中是否至少有一个True
# all：检查是否每个值都是True

import numpy as np
a = np.array([False,False,True,False])
print(a.any())
print(a.all())