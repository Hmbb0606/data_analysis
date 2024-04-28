# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm

# DataFrame是一个表格型的数据结构
# 	• 每列可以是不同的值类型（数值、字符串、布尔值等）
# 	• 既有行索引index，也有列索引columns
# 	• 可以被看做由Series组成的字典
# 创建DataFrame最常用的方法，参考读取CSV、TXT、Excel、MySQL等

import pandas as pd
dict = {
        '姓名':['孙兴华','李小龙','叶问'],
        '年龄':[20,80,127],
        '功夫':['撸铁','截拳道','咏春']
        }
data = pd.DataFrame(dict)
print(data)
print(data.dtypes)    # 返回每一列的类型
print(data.columns)   # 返回列索引，以列表形式返回：[列名1，列名2，…]
print(data.index)     # 返回行索引，（起始，结束，步长）
print(data[['姓名','年龄']])   # 返回索引和这两列数据
print(data.loc[1:3])  # 返回前3行，包括结束值

# 小结：
# 常用方法
# 数据.head( 5 ) #查看前5行
# 数据.tail( 3 ) #查看后3行
# 数据.values #查看数值
# 数据shape #查看行数、列数
# 数据.fillna(0) #将空值填充0
# 数据.replace( 1, -1) #将1替换成-1
# 数据.isnull() #查找数据中出现的空值
# 数据.notnull() #非空值
# 数据.dropna() #删除空值
# 数据.unique() #查看唯一值
# 数据.reset_index() #修改、删除，原有索引，详见例1
# 数据.columns #查看数据的列名
# 数据.index #查看索引
# 数据.sort_index() #索引排序
# 数据.sort_values() #值排序
# pd.merge(数据1,数据1) #合并
# pd.concat([数据1,数据2]) #合并，与merge的区别，自查
# pd.pivot_table( 数据 ) #用df做数据透视表（类似于Excel的数透）