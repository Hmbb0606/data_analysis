# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
数据 = pd.read_excel('./data/08.折线图.xlsx')
plt.plot(数据.时间,数据.蔬菜)
plt.plot(数据.时间,数据.水果)
#覆盖下线、覆盖上限 0,数据.蔬菜
plt.fill_between(数据.时间,0,数据.蔬菜,facecolor='r',alpha=0.3)
plt.fill_between(数据.时间,0,数据.水果,facecolor='g',alpha=0.3)
plt.show()