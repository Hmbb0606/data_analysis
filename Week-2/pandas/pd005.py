# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm

import numpy as np
import pandas as pd
data1= pd.DataFrame({'姓名':['叶问','李小龙','孙兴华','李小龙','叶问','叶问'],'出手次数1':np.arange(6)})
data2 = pd.DataFrame({'姓名':['黄飞鸿','孙兴华','李小龙'],'出手次数2':[1,2,3]})
data3 = pd.merge(data1,data2)
print(data3)

data3 = pd.merge(data1,data2,on='姓名',how='inner')

# 类似的还有左连接、右连接、全连接
# result = pd.merge(left, right, on=['key1', 'key2'])
# result = pd.merge(left, right, how='left', on=['key1', 'key2'])
# result = pd.merge(left, right, how='right', on=['key1', 'key2'])
# result = pd.merge(left, right, how='outer', on=['key1', 'key2'])
# result = pd.merge(left, right, on='k', suffixes=['_l', '_r'])