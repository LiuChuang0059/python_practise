#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 20:13:40 2018

@author: liuchuang


线性时间求解 最大子数组
"""

def Find_Maxmum_Subarray(A, low, high):
    left=0
    right=0
    sum = A[low]
    tempSum = 0
    for i in range(low,high+1):
        tempSum = max(A[i],tempSum+A[i])
        if tempSum>sum:
            sum = tempSum
            right = i
        elif tempSum == A[i]:
            left = i
    return (left,right,sum)
A=[1,-2,3,4,-4,5,6,-4,5]
print(Find_Maxmum_Subarray(A,0,8))

 