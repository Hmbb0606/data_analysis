# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
data = pd.read_excel('./data/22.雷达图.xlsx')
条件1 = "姓名=='A01'"
条件2 = "姓名=='A02'"
# print(数据.query(条件1))
A01 = data.query(条件1)['分数']
A02 = data.query(条件2)['分数']
科目 = data.query(条件1)['科目']
# 设置雷达图角度，用于平分切开一个平面 linspace(起始，结束，len(A01)个等步长的样本数量，endpoint不包括结束值)
角度 =np.linspace(0, 2*np.pi,len(A01), endpoint=False)
# 使雷达图封闭起来
A01 = np.concatenate((A01,[A01[0]]))
# print(A01)
A02 = np.concatenate((A02,[A02[0]]))
角度 = np.concatenate((角度,[角度[0]]))
科目 = np.concatenate((科目,[科目[0]]))
# 画图
布=plt.figure()
图 = 布.add_subplot(111,polar=True)
图.plot(角度,A01,'o-',linewidth=2,alpha=0.25,label='A01同学') #linewidth线粗
图.fill(角度,A01,'r',alpha=0.25)
图.plot(角度,A02,'o-',linewidth=2,alpha=0.25,label='A02同学') #linewidth线粗
图.fill(角度,A02,'b',alpha=0.25)
# 标签
图.set_thetagrids(角度 * 180 / np.pi,科目)
图.set_ylim(0,100)
plt.legend(loc='best')
plt.show()