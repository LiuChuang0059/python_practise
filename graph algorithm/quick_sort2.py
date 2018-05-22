# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:59:27 2018

@author: 刘闯

快速排序
"""

def quick_sort(arr):
    if len(arr) <2:
        return arr
    else:
        list1=[]
        list2=[]
        for i in arr[1:]:
            if i >= arr[0]:
                list1.append(i)
            else:
                list2.append(i)
    return quick_sort(list2)+[arr[0]] +quick_sort(list1)
    
list4=[13,4,3,2,3,9,3,4,5,6,76,7,3,4,5,6,6,7,8]
print(quick_sort(list4))

##重复元素无法排序
