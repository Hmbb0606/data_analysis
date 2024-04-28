# -*- codeing = utf-8 -*-
# @Time : 2024/4/21 20:10
# @Author : Li Wenhai
# @Software : PyCharm
import numpy as np
a = np.arange(10)
print(a)
c = a > 5
print(c) # 返加False和True
print(a[c]) # 返回6 7 8 9