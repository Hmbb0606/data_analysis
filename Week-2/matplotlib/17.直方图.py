# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm
import pandas as pd
import matplotlib.pyplot as plt
# 显示所有列，同理：max_rows
pd.options.display.max_columns=None
plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
数据 = pd.read_excel('./data/17.直方图.xlsx')
print(数据)
plt.hist(数据.身高,
         bins=30,
         facecolor='b',
         edgecolor='r',
         alpha=0.8)
plt.show()