# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False
数据 = pd.read_excel('./data/08.折线图.xlsx')
plt.plot(数据.时间,数据.蔬菜)
轴=plt.gca()
# 轴.set_xlim([0, 10])   #设置X轴的区间
# 轴.set_ylim([0, 100])   #Y轴区间
# 轴.axis([0, 10, 0, 100])   #X、Y轴区间 [xmin,xmax,ymin,ymax]
轴.set_ylim(bottom=-10)     #Y轴下限
轴.set_xlim(right=25)       #X轴上限
plt.show()