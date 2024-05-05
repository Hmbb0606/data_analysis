# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文

布 = plt.figure()

plt.subplot(221)
plt.plot(["A","B","C"],[1,2,3],'ro-')
plt.title("李文海图1",c='b')
# 字典=dict(facecolor='yellow', pad=5, alpha=0.2)
#pad是填充大小
plt.xlabel("x轴",bbox={'facecolor':'yellow','pad':5,'alpha':0.2})

plt.subplot(222)
plt.subplot(223)
plt.subplot(224)
# 整个画板的标题
plt.suptitle("李文海",fontsize=16,fontweight='bold',color='r')
# wspace子图之间的宽度，hspace子图之间的高度，left代表子图与布的左边距离
plt.subplots_adjust(left=0.2,top=0.8,wspace=0.8,hspace=0.8,bottom=0.1)
plt.show()