# -*- coding: utf-8 -*-
"""
Created on Sat May 26 18:21:35 2018

@author: 刘闯

动态规划
在重量允许下 价格总和最大

"""

##创建表示物品价格 和 重量的字典
goods={}
goods['guita']=[1,1500]
goods['notebook']=[3,2000]
goods['sounder']=[4,3000]

###数字和物品 对应字典
num={}
num[1]='guita'
num[2]='notebook'
num[3]='sounder'

###创建价格表格 

price={}
for i in range(1,len(goods.keys())+1):
    for j in range(1,5):
        price[i][j]=0
        if goods[i][0]<j:
            price[i][j]=max(price[i-1][j],goods[num[i]][1]+price[i-1][j-goods[num[i]][0])
               