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
data = pd.read_excel('./data/07.饼图.xlsx')
plt.pie(x=data.第一次,
        labels=tuple(data.姓名),
        explode=(0, 0.2, 0),
        colors=['r', 'g', 'b'],
        autopct='%.2f%%',
        startangle=90,
        counterclock=False,
        labeldistance=0.8,
        radius=1.3,
        # pctdistance=0.3,# ???
        textprops={'fontsize':20,'color':'w'}
        )
#将饼图变成正圆
plt.axis('equal')
plt.legend(loc='upper right',
           fontsize=10,
           bbox_to_anchor=(1.1, 1.05),
           borderaxespad=0.3,
           ncol=3)
plt.savefig("./pie.jpg",dpi=200)
plt.show()