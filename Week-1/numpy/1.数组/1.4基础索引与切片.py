# -*- codeing = utf-8 -*-
# @Time : 2024/4/21 19:52
# @Author : Li Wenhai
# @Software : PyCharm
import numpy as np
a = np.arange(10)                        # 一维数组使用小写
b = np.arange(20).reshape(4,5)           # 多维数组使用大小

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a[3],a[5],a[-1])    # 返回 3 5 9
print(a[2:4])   # 返回 array([2, 3]) 切片

print('*'*50)

A = np.arange(20).reshape(4,5)
print(A)

print('*'*50)

print(A[0,0])      # 取数组A的0行0列，返回值0
print(A[-1,2])     # 取最后一行的第2列，返回值17
print(A[2])        # 取第2行所有的列，返回array([10, 11, 12, 13, 14])
print(A[-1])       # 取最后1行
print(A[0:-1])     # 取除了最后1行之外其它所有行 ???
print(A[0:2,2:4])  #取0和1行，2和3列
print(A[:,2])      # 取所有行中的第2列

print('*'*50)

A[:1,:2]=520      # 修改0行0 1列的两个值
print(A)