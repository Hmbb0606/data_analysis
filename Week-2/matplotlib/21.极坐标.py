# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm
import matplotlib.pyplot as plt
import numpy as np
#风格
plt.style.use('ggplot')
angle = np.array([0.25, 0.75, 1, 1.5,0.25])
rou = [20, 60, 40, 80, 20]
plt.polar(angle*np.pi, rou, 'ro-',)
plt.fill(angle*np.pi, rou, 'r', alpha=0.75) #alpha透明度
plt.ylim(0,100)
plt.show()