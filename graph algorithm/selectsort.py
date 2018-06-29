#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 23:34:38 2018

@author: liuchuang


选择排序  

每次遍历 只交换一次

共n-1次遍历

O(N^2)


"""

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        position_of_max = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[position_of_max]:
                ##确定最大值的位置
                position_of_max = location
        
        temp = alist[fillslot]
        ### 与最后的位置交换
        alist[fillslot] = alist[position_of_max]
        alist[position_of_max] = temp



alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)