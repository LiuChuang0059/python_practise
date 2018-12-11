#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 00:14:35 2018

@author: liuchuang
"""


import numpy as np


a = np.arange(10)

### 1 通过下标范围产生数组  和原数组共享数据空间
b=a[::-1]  ## 步长为负数 倒序
c=a[3:7]   ### 左开右闭


### 2 通过整数序列 元素选取 每个元素作为下标  获得新数组 不共享空间

d=a[[1,2,3,5]]
a[[1,2,3]]=4,5,6


print(a,b,c,d)


### 3 布尔数组

e = np.arange(3)
f=e[np.array([True,False,True])]
print('\n\n')
print(f)