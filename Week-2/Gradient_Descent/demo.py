# -*- codeing = utf-8 -*-
# @Time : 2024/4/27 21:29
# @Author : Li Wenhai
# @Software : PyCharm

import matplotlib.pyplot as plt

x_data = [1.0,2.0,3.0]
y_data = [2.0,4.0,6.0]
w=1.0

# 前向传播过程
def forward(x):
    print(x*w)
    return x*w


# cost为数据集中所有样本的误差值平方再求均值
def cost(xs,ys):
    cost = 0
    for x,y in zip(xs,ys):
        y_pred = forward(x)
        cost += (y_pred - y) ** 2
    return cost/len(xs)

# 计算梯度时为所有样本的平均梯度
def gradient(xs,ys):
    grad = 0
    for x,y in zip(xs,ys):
        grad+= 2*x*(x*w-y)
    return grad/len(xs)

#画图
w_list = []
cost_list = []
w_list.append(0.1)
for epoch in range(101):
    cost_val = cost(x_data,y_data)
    grad_val = gradient(x_data,y_data)
    w-=0.01*grad_val
    w_list.append(w)
    cost_list.append(cost_val)
    print('Epoch:',epoch,'w=',w,'loss',cost_val)

plt.plot(range(101),cost_list)
plt.xlabel('epoch')
plt.ylabel('cost')
plt.show()
