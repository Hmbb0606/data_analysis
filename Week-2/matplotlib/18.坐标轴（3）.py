# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm
import pandas as pd
import matplotlib.pyplot as plt

#将x轴平均分成五份

plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
数据 = pd.read_excel(r'./data/17.直方图.xlsx')
布, 图 = plt.subplots(1,1)
图.plot(数据.序号,数据.身高)
# 第一种方法：
# plt.locator_params("x", nbins = 5)
# 第二种方法：
轴 = plt.gca()  # 获取当前轴
#轴.locator_params("x", nbins=5)
# x与y都平均分成5份
轴.locator_params(nbins=5)
plt.show()
