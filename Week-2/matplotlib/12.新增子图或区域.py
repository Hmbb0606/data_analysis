# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
数据 = pd.read_excel('./data/09.折线与柱状组合图.xlsx')

布 = plt.figure()

left,bottom,width,height = 0.1,0.1,0.8,0.8
# 参数是一个列表，距左和下的距离，以及自身的宽和高度
图1 = 布.add_axes([left,bottom,width,height])
图1.bar(数据.班级,数据.销售量)
图1.set_title("销售量")

left,bottom,width,height = 0.65,0.6,0.25,0.25
图2 = 布.add_axes([left,bottom,width,height])
图2.plot(数据.班级,数据.毛利率)
图2.set_title("毛利率")

plt.show()