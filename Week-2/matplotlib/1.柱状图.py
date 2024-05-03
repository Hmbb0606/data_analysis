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
# print(data)

#横纵坐标名称
plt.xlabel("姓名")
plt.ylabel("分数")

#横坐标旋转45° error
plt.xticks(rotation=45)

#y轴的范围
plt.ylim([-30, 120])

#x，y轴各是什么，显示图例
plt.bar(data.姓名, data.分数, label="成绩")

#图例位置
plt.legend(loc="upper left")
#布局
plt.tight_layout()

#加标题
plt.title("三年二班学生成绩",fontsize=16,fontweight='bold')
plt.show()