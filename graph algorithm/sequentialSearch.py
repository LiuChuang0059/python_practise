#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 22:55:03 2018

@author: liuchuang


顺序查找

按照基本的顺序排序


从一项移动到 另一项

直到找到 正在寻找的项
"""

def sequentialSearch(list1,item):
    """
    
    """
    pos=0
    found = False
    
    
    while pos < len(list1) and not found :
        if list1[pos] == item:
            found = True
            
        else:
            pos += 1
            
    return found


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))