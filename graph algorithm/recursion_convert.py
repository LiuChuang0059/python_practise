#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 23:41:12 2018

@author: liuchuang



递归 解决


整数转化为任意进制的字符串


"""

def convert(n,base):
    convertstring = "0123456789ABCDEF"
    if n < base :  ###基本条件
        return convertstring[n]
    else:   ###递归调用
        return convert(n//base,base) + convertstring[n%base]
    
print(convert(6137,2))