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
# print(data)
# 柱图
plt.bar(data.班级,
        data.销售量,
        color='r',
        label='销售量',
        alpha=0.6)
# 显示图例
plt.legend()
# 平均线-折线图
avg = np.mean(data.销售量)
plt.axhline(y=avg,
            color="blue",
            linestyle=':')
plt.show()