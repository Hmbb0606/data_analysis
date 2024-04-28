# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm

# pd.read_excel参数：
# skiprows=行数          #跳过几行
# usecols="区域"         # 和Excel中一样，就是一个列的区域
# index_col="字段名"        # 将谁设置为索引
# dtype={'序号':str,'性别':str,'日期':str}   # 防止出错，把类型全指定为字符型
# 数据.at的用法
# 作用：获取某个位置的值，例如，获取第0行，第a列的值，即：index=0，columns='a'
# 变量名 = 数据.at[0, 'a']

import pandas as pd
import datetime as 日期模块
路径 = 'F:\Pycarm\Project\data_analysis\Week-2\pandas\lwh.xlsx'
起始日期 = 日期模块.date(2020,1,1)
读取数据 = pd.read_excel(路径,skiprows=2,usecols="B:E",index_col=None,dtype={'序号':str,'性别':str,'日期':str})
for i in 读取数据.index:
    读取数据['序号'].at[i] = i+1
    读取数据['性别'].at[i] = '男' if i%2 == 0 else '女'
    读取数据['日期'].at[i] = 起始日期 + 日期模块.timedelta(days=i)  # timedelta只能加天，小时，秒，毫秒
    读取数据['日期'].at[i] = 日期模块.date(起始日期.year+i,起始日期.month,起始日期.day) # 如果要在年上累加用date
print(读取数据)