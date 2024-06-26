# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm
import matplotlib.pyplot as plt

left  = 0.125  # 图片中子图的左侧
right = 0.9    #图片中子图的右侧
bottom = 0.1   # 图片中子图的底部
top = 0.9      # 图片中子图的顶部
wspace = 0.2 #为子图之间的空间保留的宽度，平均轴宽的一部分
hspace = 0.2  #为子图之间的空间保留的高度，平均轴高度的一部分

布,图=plt.subplots(2,2)
# wspace子图之间的宽度，hspace子图之间的高度，left代表子图与布的左边距离
布.subplots_adjust(wspace=0.5, hspace=0.3,left=0.125, right=0.9,top=0.9,bottom=0.1)
plt.show()