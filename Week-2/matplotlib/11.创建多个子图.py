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

bu = plt.figure(num='李文海',
                figsize=(12, 13),
                dpi=200,
                facecolor='b')

plt.show()