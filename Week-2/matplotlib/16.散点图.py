# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
数据 = pd.read_excel('./data/16.散点图.xlsx')
# plt.scatter(data.身高,
#             data.体重,
#             s=data.身高,
#             c='b',
#             marker='o',
#             alpha=0.6,
#             linewidths=20)
plt.scatter(数据.身高,数据.体重,s=数据.身高,c=数据.身高)
plt.colorbar() # 添加颜色栏
plt.show()