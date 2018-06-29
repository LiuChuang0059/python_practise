#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 21:12:59 2018

@author: liuchuang


使用栈 进行十进制和二进制 之间的 转换

以及任意进制件的 转换


"""
from pythonds.basic.stack import Stack

def dividedBy2(decnumber):
    """
    二进制构建数字序列 
    第一个余数是序列的最后一个数字
    """
    remstack = Stack()
    
    while decnumber > 0 :
        rem = decnumber % 2  ### 余数
        remstack.push(rem)  ### 存入栈底
        decnumber = decnumber // 2  
    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())  ## 调用栈
    
    return binString

print(dividedBy2(134))
        


"""
除 2 更改为 除以 base
进行 任何基数的转换

"""


def dividedByBase(decnumber,base):
    """
    构建数字序列 
    第一个余数是序列的最后一个数字
    """
    remstack = Stack()
    
    while decnumber > 0 :
        rem = decnumber % base  ### 余数
        remstack.push(rem)  ### 存入栈底
        decnumber = decnumber // base 
    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())  ## 调用栈
    
    return binString

print(dividedByBase(134,10))

print(dividedByBase(134,16))






























