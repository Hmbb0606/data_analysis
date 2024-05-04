# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
data = pd.read_excel('./data/12.日期.xlsx')
#(1)
# plt.plot(data.日期, data.销售)
# plt.show()
#(2)
# 数据 = [d for d in data.日期]
日期 = [d.strftime('%Y-%m-%d') for d in data.日期]
plt.plot(日期,data.销售)
plt.xticks(日期,rotation=45)
plt.show()