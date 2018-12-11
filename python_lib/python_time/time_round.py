#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 00:44:12 2018

@author: liuchuang


round()

function  四舍五入

传入两个  一个 为需要修改的小数
一个为需要保留的位数（ 默认值为0）



"""

import time 

now = time.time()

time1 = round(now) ## 保留到整数

time2 = round(now,3) ### 保留小数点后  n位 小数

print(str(time1)+ '\n'+str(time2))