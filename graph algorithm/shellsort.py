#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:35:09 2018

@author: liuchuang


希尔排序

"""



def shellSort(alist):
    ###分割成 多个等大的 子列
    sublist = len(alist)//2 
    
    while sublist > 0:
        for startposition in range(sublist):
            gapInsertSort(alist,startposition,sublist)
        
        sublist = sublist // 2  ##增加 排序 子列len数  规模
    
    
def gapInsertSort(alist,start,gap):
    ##间隔的插入排序
    for i in range(start+gap,len(alist),gap):
        current = alist[i]
        position = i
        
        while position >=gap and alist[position-gap] > current:
            ##左边的值较大
            alist[position] =alist[position-gap]###左边值先移到 现在的位置
            position = position - gap ###现在小的位置为  前一个位置
            
        alist[position] = current  ##将刚刚的值 移动
            
alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)    