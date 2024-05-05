# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
x= ["A","B","C","D","E","F"]
y= [1,10,7,5,11,6]
# drawstyle有steps、steps-pre、steps-mid、steps-post和默认共5种
plt.plot(x,y,"r-",drawstyle='steps')
plt.show()