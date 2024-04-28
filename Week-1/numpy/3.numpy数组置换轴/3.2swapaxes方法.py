# -*- codeing = utf-8 -*-
# @Time : 2024/4/21 20:50
# @Author : Li Wenhai
# @Software : PyCharm
import numpy as np
a = np.arange(24).reshape((4,6))
print(a)
print("-"*30)
print(a.swapaxes(1,0))