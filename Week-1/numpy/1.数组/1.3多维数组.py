# -*- codeing = utf-8 -*-
# @Time : 2024/4/21 18:26
# @Author : Li Wenhai
# @Software : PyCharm
import numpy as np

a = np.ones(3)
b = np.ones((2,3))
c = np.ones((5,), dtype=int)

print(a)
print(b)
print(c)

a = np.array([1,2,3,4,5,6])
b = np.array(
    [
        [1,2,3],
        [4,5,6]
    ]
)
print(a)
print(b)