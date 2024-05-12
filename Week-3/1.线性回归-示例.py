# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('data/generated_data.csv')
x = data.loc[:, 'x']
y = data.loc[:, 'y']
plt.figure(figsize=(20,20))
plt.scatter(x, y)
# plt.show()

lr_model = LinearRegression()
x = np.array(x) #此时x为一维数组 (10, 1)
x = x.reshape(-1,1)
y = np.array(y) #此时y为一维数组 (10,)
y = y.reshape(-1,1)

print(type(x),x.shape,type(y),y.shape)
# <class 'numpy.ndarray'> (10, 1) <class 'numpy.ndarray'> (10, 1) 10行1列
print('*'*50)
print(type(x),x.shape)


lr_model.fit(x,y)
# 直接预测x
y_predict = lr_model.predict(x)
print(y_predict)
# 预测[[3.5]]
y_3 = lr_model.predict([[3.5]])
print(y_3)
print(y)



