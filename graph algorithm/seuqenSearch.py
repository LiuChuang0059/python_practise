#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 23:04:58 2018

@author: liuchuang



如果 列表排序  假设升序

进行搜索


"""
def orderedSequentialSearch(list2,item):
    
    
    pos = 0
    found = False
    stop = False
    
    
    while pos < len(list2) and not found and not stop :
        if list2[pos]  == item:
            found = True
            
        elif list2[pos] > item:
            stop = True
        else:
            pos = pos+1
                
    return found



testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))