# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm

import numpy as np
arr = np.arange(9).reshape((3,3))
print(arr)
arr1 = np.concatenate([arr,arr],axis=1)
print(arr1)
arr2 = np.concatenate([arr,arr],axis=0)
print(arr2)

import pandas as pd
data1 = pd.Series([0,1,2],index=['A','B','C'])
data2 = pd.Series([3,4],index=['D','E'])
data3 = pd.concat([data1,data2])
print(data3)

# 汇总
# concat：可以沿一条轴将多个对象连接到一起
# merge：可以根据一个或多个键将不同的DataFrame中的行连接起来。
# join：inner是交集，outer是并集。