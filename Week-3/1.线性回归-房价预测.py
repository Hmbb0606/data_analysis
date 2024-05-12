# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm
# 加载数据
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

# 基于 usa_housing _price.csv 数据,建立线性回归模型，预测合理房价:
# 1、以面积为输入变量，建立单因子模型, 评估模型表现，可视化线性回归预测结果
# 2、以income、house age、numbers of rooms、population、area为输入变量，建立多因子模型，评估模型表现
# 3、预测 Income=65000,，House Age=5, Number of Rooms=5, Population=30000, size=200的合理房价

data = pd.read_csv('./data/usa_housing_price.csv')

#数据散点图展示
# fig = plt.figure(figsize=(10,10))
# fig1 =plt.subplot(231)
# plt.scatter(data.loc[:,'Avg. Area Income'],data.loc[:,'Price'])
# plt.title('Price VS Income')
#
# fig2 =plt.subplot(232)
# plt.scatter(data.loc[:,'Avg. Area House Age'],data.loc[:,'Price'])
# plt.title('Price VS House Age')
#
# fig3 =plt.subplot(233)
# plt.scatter(data.loc[:,'Avg. Area Number of Rooms'],data.loc[:,'Price'])
# plt.title('Price VS Number of Rooms')
#
# fig4 =plt.subplot(234)
# plt.scatter(data.loc[:,'Area Population'],data.loc[:,'Price'])
# plt.title('Price VS Area Population')
#
# fig5 =plt.subplot(235)
# plt.scatter(data.loc[:,'size'],data.loc[:,'Price'])
# plt.title('Price VS size')
# plt.show()

#定义 x 和 y
X = data.loc[:,'size']
y = data.loc[:,'Price']
# print('*'*50)
# print(y.shape)

# 转换维度
X = np.array(X).reshape(-1,1)
y = np.array(y).reshape(-1,1)
# print(X.shape)

#线性回归模型
LR1 = LinearRegression()
LR1.fit(X,y)

#预测
y_predict_1 = LR1.predict(X)
print(y_predict_1)

#模型评估
mean_squared_error_1 = mean_squared_error(y,y_predict_1)
r2_score_1 = r2_score(y,y_predict_1)
print(mean_squared_error_1,r2_score_1)

# 绘图
fig6 = plt.figure(figsize=(8,5))
plt.scatter(X,y)
plt.plot(X,y_predict_1,'r')
plt.show()
