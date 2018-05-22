# -*- coding: utf-8 -*-
"""
Created on Thu May 17 22:36:20 2018

@author: 刘闯

选择排序

"""

#遍历 寻找最小值
def find_smallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(0,len(arr)):## range到len-1
        if smallest>=arr[i]:
            smallest=arr[i]
            smallest_index=i
    return smallest_index


#将最小值 依次放入新的列表

def select_sort(arr):
    new_arr=[]
    while len(arr)>0:
        s=find_smallest(arr)
        t=arr.pop(s)
        new_arr.append(t)
    return new_arr

list2=[2,34,56,23,43,555,86,45,777,1,333,44445,0,1,2]
print(select_sort(list2))


list2.sort()##list已经pop删除清空
print(list2)


    
