#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 16:16:52 2018

@author: liuchuang

最大子数组问题

"""

def Find_Max_Crossing_Subarray(A,low,mid,high):
    if len(A)/2==0:
        mid=int(len(A)/2)
    else:
        mid=int((len(A)-1)/2)
    left_sum=float('-inf')
    sum=0
    left_index=mid
    list1=list(range(mid+1))
    list1.reverse()
    for i in list1:
        sum=sum+A[i]
        if sum> left_sum :
            left_sum=sum
            left_index=i
    right_sum=float('-inf')
    sum=0
    right_index=mid+1
    for j in range(mid+1,high+1):
        sum=sum+A[j]
        if sum> right_sum :
            right_sum=sum
            right_index=j
    return(left_index,right_index,left_sum+right_sum)
A=[-2,3,4,-1,-5,4,-5]
print(Find_Max_Crossing_Subarray(A,0,3,6))