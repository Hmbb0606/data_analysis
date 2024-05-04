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
data = pd.read_excel('./data/09.折线与柱状组合图.xlsx')

bu = plt.figure()
one = bu.add_subplot(221) #2x2 第一个图
plt.bar(data.班级, data.销售量)
two = bu.add_subplot(222)
three = bu.add_subplot(223)
plt.plot(data.班级,
         data.毛利率,
         label='毛利率',
         color='r',
         marker='*',
         ms=10)
four = bu.add_subplot(224)
plt.plot(data.班级, data.毛利率)
plt.show()
