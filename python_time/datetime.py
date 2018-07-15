#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 01:25:13 2018

@author: liuchuang


datetime module

"""

import datetime
import time

## 1  datetime 数据类型


dt = datetime.datetime.now()  ## 返回一个 datetime 对象

dt1 = datetime.datetime(2018,7,15,1,37,0)  ##传入数据

print(dt1.year,dt1.month,dt1.day)

print(dt1.second)

# datetime 对象可以进行比较  

datetime.datetime.fromtimestamp(time.time())# Unix 纪元时间 转换为本地时间

## 2 tiemdelta 数据类型 ： 表示一段时间 

delta = datetime.timedelta(days=3,hours=4,minutes=4,seconds=4)
#datetime.timedelta()函数 接受关键字参数 weeks、days、hours、minutes、seconds、milliseconds 和 microseconds

print(delta.seconds)   # 不包括天数的总秒数
print(delta.total_seconds()) ## 包括天数的 总秒数 
print(str(delta))  ## 返回格式良好的 时间


## 3 datetime 和dtime delta  进行日期计算

dt2= datetime.datetime.now()
delta2 = datetime.timedelta(days = 1000)
print(dt2 + delta2) ## 计算10000 天之后的日期

## 4 time.sleep()  datetime   暂停到特定的时间
"""
dt3 = datetime.datetime(2018,7,18,0,0,0)
while datetime.datetime() < dt3:
    time.sleep(1)
"""

## 5 datetime 对象 和字符串相互转化
### 1 datetime 转换字符串 

today = datetime.datetime(2018,7,15,2,9,8)
print(today.strftime('%Y%m%d'))
print(today.strftime('%I:%M,%p'))


### 2 字符串 转换为 datetime

datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')# 类似于正则变换

datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S') # 准确匹配





























