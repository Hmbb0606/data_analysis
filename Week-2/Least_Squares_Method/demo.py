# -*- codeing = utf-8 -*-
# @Time : 2024/4/27 22:30
# @Author : Li Wenhai
# @Software : PyCharm
#线性，最小二乘法
import numpy as np
import matplotlib.pyplot as plt

x_data=[1.0,2.0,3.0]
y_data=[2.0,4.0,6.0]

#定义模型
def forward(x):
    return x*w

#定义损失函数
def loss(x,y):
    y_pred=forward(x)
    return (y_pred-y)*(y_pred-y)

#存储w权重，并记录下对应的cost value
w_list=[]
mse_list=[]

#权重从0，到4，步长为0.1
for w in np.arange(0.0,4.1,0.1):
    print("w=",w)
    l_sum=0
    for x_val,y_val in zip(x_data,y_data):
        y_pred_val=forward(x_val)
        loss_val=loss(x_val,y_val)
        l_sum+=loss_val
        print("\t",x_val,y_val,y_pred_val,loss_val)
    print("mse=",l_sum/3)
    w_list.append(w)
    mse_list.append(l_sum/3)

plt.plot(w_list,mse_list)
plt.ylabel("loss")
plt.xlabel("w")
plt.show()

# step1: 定义模型结构
# step2: 构造损失函数
# step3: 不断调参知道损失函数的值降到最小
