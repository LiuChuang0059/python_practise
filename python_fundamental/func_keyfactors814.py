# -*- coding: utf-8 -*-
"""
Created on Mon May 14 22:27:54 2018

@author: lc

函数接受 任意关键实参
"""

def make_car(name,type,**infor):##**infor接受任意键值
    car={}
    car['name']=name
    car['type']=type
    for k,v in infor.items():
        car[k]=v
    return car
A=make_car('dazhong','car',color='black',size='small')
print(A)
