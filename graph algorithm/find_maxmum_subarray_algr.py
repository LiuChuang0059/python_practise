#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 18:42:32 2018

@author: liuchuang


最大子数组

"""
from find_maxmum_subarray_alg import Find_Max_Crossing_Subarray as fmcs

def Find_Maxmum_Subarray(A,low,high):
    ##基本情况
    if high==low:
        return (low,high,A[low])
    else:
        
        mid=int((low+high)/2)
        """
        left_low=Find_Maxmum_Subarray(A,low,mid)[0]
        left_high=Find_Maxmum_Subarray(A,low,mid)[1]
        left_sum=Find_Maxmum_Subarray(A,low,mid)[2]
        right_low=Find_Maxmum_Subarray(A,mid+1,high)[0]
        right_high=Find_Maxmum_Subarray(A,mid+1,high)[1]
        right_sum=Find_Maxmum_Subarray(A,mid+1,high)[2]
        cross_low=fmcs(A,low,mid,high)[0]
        cross_high=fmcs(A,low,mid,high)[1]
        cross_sum=fmcs(A,low,mid,high)[2]
        """
        
        ### 左数组
        (left_low,left_high,left_sum)=Find_Maxmum_Subarray(A,low,mid)
        ###右数组
        (right_low,right_high,right_sum)=Find_Maxmum_Subarray(A,mid+1,high)
        ### 包含中点 调用
        (cross_low,cross_high,cross_sum)=fmcs(A,low,mid,high)
        
        ####比较
        if left_sum>=right_sum and left_sum>=cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum>=left_sum and right_sum>=cross_sum:
            return(right_low,right_high,right_sum)
        else:
            return(cross_low,cross_high,cross_sum)

A=[-1,-3,3,4,6,3,4,53,-4,-7,4,5,6,-5,-6]
print(Find_Maxmum_Subarray(A,1,12))