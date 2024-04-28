# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm

import pandas as pd

# 新建空白Excel文件
path = 'F:\Pycarm\Project\data_analysis\Week-2\pandas\lwh.xlsx'
# DataFrame是一个表格型的数据结构
data = pd.DataFrame()
data.to_excel(path)
print('新建Excel成功')

