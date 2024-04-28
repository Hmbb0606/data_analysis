# -*- codeing = utf-8 -*-
# @Author : Li Wenhai
# @Software : PyCharm
import pandas as pd
data = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['a','b','c'])
print(data)
print(data['a'][0] )
print(data.loc[0]['a'] )
print(data.iloc[0][0] )
print(data[['a','b']])