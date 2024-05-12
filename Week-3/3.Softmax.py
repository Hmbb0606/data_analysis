# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm

import torch
from d2l import torch as d2l
import matplotlib.pyplot as plt

batch_size = 256
num_inputs = 28*28
num_output = 10
lr = 0.1
num_epochs = 10

# 1.定义参数 更新的参数


# 2.加载我们的dataset dataloader


# 3，定义我的softmax函数


# 4.定义我们的模型


# 5.定义交叉熵损失函数


# 6.定义优化器


# 7.进行数据集的训练和预测



if __name__ == '__main__':
    X = torch.linspace(1, 6, steps=6).view(2, 3)
    X = torch.randn((2, 5))
    y= torch.randn((2, 5))
    y_hat = torch.tensor([[0.1, 9.3, 0.6], [0.3, 0.2, 0.5]])