#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 23:05:16 2018

@author: liuchuang


冒泡排序
"""

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        ###排序数目递减
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp ##交换位置

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
                