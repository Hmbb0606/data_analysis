# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
data = pd.read_excel('./data/12.日期.xlsx')
plt.plot(data.日期, data.销售)
plt.grid(axis='x',
         color='r',
         linestyle=':',
         linewidth=3)
plt.show()