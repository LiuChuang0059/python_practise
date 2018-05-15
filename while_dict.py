# -*- coding: utf-8 -*-
"""
Created on Mon May 14 17:38:13 2018

@author: lc

while 填充字典
扩展 多个人 字典添加列表
"""

dp={} #空储存字典
place=[]#空列表
p1="\nWhat is your name        :    "
p2="\nWhere would you go       :    "
p3="\nwhereelse would you go   :    "
p4="\nDo you want to another(y/n)   :    "  
p5="\nAnother one(y/n)?"

#设置标志位 
A=True
while A :
    name=input(p1)
    place1=input(p2)
    ask=input(p4)
    if ask =='y': #个人列表
        place2=input(p3)
        place.append(place1)
        place.append(place2)
        dp[name]=place
    else:
        dp[name]=place1
    repeat=input(p5)
    if repeat=='n': ##多人重复
        A=False

#打印结果
print("\n ----POll list----")
for k,v in dp.items():
    if type(v)!=str:  ##不能用len（）进行判断 因为 字符列表都有长度
        for i in v:
            print(k  +  " would like to go to :  " + i)
    else:
        print(k  +  " would like to go to :  " + v)

        
    