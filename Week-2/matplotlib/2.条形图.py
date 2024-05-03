# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm
import pandas as pd
import matplotlib.pyplot as plt
#正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
#正常显示负号
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_excel('./data/01.柱状图.xlsx')
#inplace代表原数据修改，ascending代表降序
data.sort_values(by='分数', inplace=True, ascending=False)

plt.bar(x=0,
        bottom=data.姓名,
        height=0.5,
        width=data.分数,
        color='red',
        orientation='horizontal',
        alpha=0.5 #透明度
)
plt.ylabel("姓名", fontsize=20)
plt.xlabel("分数", fontsize=20)
plt.title("三年二班学生成绩",fontsize=16,fontweight='bold')

plt.show()
