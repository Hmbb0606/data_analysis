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

data = pd.read_excel('./data/03.分组柱状图.xlsx')

data.sort_values(by='第二年', inplace=True, ascending=False)

w=0.3
plt.bar(x=data.姓名,
        height=data.第一年,
        color='red',
        width=w,
        label="第一年")
plt.bar(x=np.arange(len(data.姓名))+w,
        height=data.第二年,
        color='blue',
        width=w,
        label="第二年")
plt.legend()

plt.xticks(data.姓名)
zhou = plt.gca()
zhou.set_xticklabels(data.姓名,
                     rotation = 45,
                     ha = "center")
#图形的边距设置
tuxing = plt.gcf()
tuxing.subplots_adjust(left=0.1,bottom=0.3)
for x,y1 in enumerate(data.第一年):
    plt.text(x, y1/2, str(y1), fontsize=20, rotation=0, ha='center', va='bottom',color='blue')
for x, y2 in enumerate(data.第二年):
    plt.text(x+w, y2 / 2, str(y1), fontsize=20, rotation=0, ha='center', va='bottom')

plt.show()





