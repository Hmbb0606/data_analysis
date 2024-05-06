# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm

# Softmax函数可以将上一层的原始数据进行归一化，转化为一个0-1之间的数值，
# 这些数值可以被当做概率分布，用来作为多分类的目标预测值。
# Softmax函数一般作为神经网络的最后一层，接受来自上一层网络的输入值，然后将其转化为概率。

import numpy as np
import numpy as np

def softmax(z):
    e_z = np.exp(z - np.max(z)) # 减去最大值，防止指数溢出
    return e_z / e_z.sum(axis=0)

# 示例
z = np.array([2.0, 1.0, 0.1])
print(softmax(z))


