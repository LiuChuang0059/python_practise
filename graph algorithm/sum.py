# -*- coding: utf-8 -*-
"""
Created on Fri May 18 11:57:06 2018

@author: 刘闯
sum：
"""

def my_sum(arr):
    if len(arr)==0:
        return 0
    elif len(arr)==1:
        return arr[0]
    else:
        arr.pop(0)
        return arr.pop(0)+sum(arr)
list3=[1,5,4]
print(my_sum(list3))