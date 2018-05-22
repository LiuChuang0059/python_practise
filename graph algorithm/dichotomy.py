# -*- coding: utf-8 -*-
"""
Created on Thu May 17 18:06:59 2018

@author: 刘闯
"""
##二分法搜寻有序数组数字位置

def search_number(list,guess):
    low=0
    high=len(list)-1
    
    
    while low<=high :   ##注意取等
        mid=(low+high)//2 ##返回伤的整数部分
        if guess==list[mid]:
            return mid
        elif guess< list[mid]:
            high=mid-1
        elif guess>list[mid]:
            low=mid+1
        else:
            return None
        
list1=[1,3,4,6,7,8,9]
print(search_number(list1,8))
print(search_number(list1,10))