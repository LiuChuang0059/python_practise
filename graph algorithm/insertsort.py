#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 00:17:01 2018

@author: liuchuang


插入排序
n-1 次比较

O(n^2)

但是仅仅进行一次分配 
"""

def insertSort(alist):
    for index in range(1,len(alist)):
        ##遍历列表
        current = alist[index]
        position = index
        
        while position > 0 and alist[position-1] > current:
            ###向左移动比较   如果小  就移位  直到大
            alist[position] = alist[position - 1]
            position = position -1
            
        alist[position]= current
        

alist = [54,26,93,17,77,31,44,55,20]
insertSort(alist)
print(alist)        