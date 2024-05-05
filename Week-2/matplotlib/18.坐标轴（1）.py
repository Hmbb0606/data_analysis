# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm
import matplotlib.pyplot as plt
# 轴的颜色
布, 图 = plt.subplots(1,1)
图.spines['left'].set_color('g')
图.spines['bottom'].set_color('r')
图.spines['top'].set_color('none')
图.spines['right'].set_color('none')

图.xaxis.set_ticks_position('top')   # x轴显示在顶部

# 图.set_xticks([])
# 图.set_yticks([])

plt.show()