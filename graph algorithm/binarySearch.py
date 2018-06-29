#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 23:23:09 2018

@author: liuchuang


二分查找

"""

def binarySearch(list1,item):
    
    first = 0 
    last = len(list1) - 1
    found = False
    
    while first < last and not found:
        midpoint = (first + last)//2
        if list1[midpoint] == item :
            found = True
        else:
            if midpoint > item :
                last = midpoint -1 
            else:
                first = midpoint + 1
                
    return found



"""

##递归

def binarySearch(alist, item):
        if len(alist) == 0:
            return False
        else:
            midpoint = len(alist)//2
            if alist[midpoint]==item:
              return True
            else:
              if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
              else:
                return binarySearch(alist[midpoint+1:],item)
 """           

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))