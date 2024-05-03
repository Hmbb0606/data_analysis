# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
#正常显示负号
plt.rcParams['axes.unicode_minus'] = False
data = pd.read_excel('./data/04.堆叠柱状图.xlsx')
# print(data)
plt.bar(np.arange(9), data.语文, color='red', label='语文')
plt.bar(np.arange(9), data.数学, bottom=data.语文, color='blue', label='语文')
plt.bar(np.arange(9), data.英语, bottom=data.语文+data.数学, color='green', label='语文')
plt.xticks(np.arange(9), data.姓名)
plt.legend(loc='upper center', ncol=3)
#y轴刻度
plt.ylim([10,350])
#绘制数值
for x1,y1 in enumerate(data.语文):
    plt.text(x1, y1-20, str(y1), color='blue', fontsize=20, ha='center')
for x2,y2 in enumerate(data.语文+data.数学):
    plt.text(x2, y2-20, str(y2), color='white', fontsize=20, ha='center')
for x3,y3 in enumerate(data.语文+data.数学+data.英语):
    plt.text(x3, y3-20, str(y3), color='black', fontsize=20, ha='center')

#网格线
# plt.grid()
plt.show()
