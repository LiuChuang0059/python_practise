#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 00:06:09 2018

@author: liuchuang

time 模块学习

"""

import time

## 1 time.time() function 
 

print(time.time())
#返回值是 Unix 纪元的那一刻与 time.time()被调用的那一刻之间的秒数

### 1 测量一段代码运行的时间


def test1():
    number = 1
    
    for i in range(1,100000):
        number = number * i
        
    return number 

starttime= time.time()
num=test1()
endtime = time.time()
costtime = endtime - starttime

print("costtime:%s" %costtime)
print(len(str(num)))