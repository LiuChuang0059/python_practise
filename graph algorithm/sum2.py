# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:13:02 2018

@author: 刘闯
sum
"""

def my_sum(arr):
    if len(arr)==0:
        return 0
    elif len(arr)==1:
        return arr[0]
    else:
        t=arr.pop(0)  ### 如果不引入变量t  将 再删除一次
        return t+sum(arr)
list3=[4,5,3]
print(my_sum(list3))