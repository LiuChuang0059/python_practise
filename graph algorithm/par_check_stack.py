#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 22:05:09 2018

@author: liuchuang

栈 实现括号的检查

从空栈开始，从左到右处理括号字符串。
如果一个符号是一个开始符号，将其作为一个信号，
对应的结束符号稍后会出现。
另一方面，如果符号是结束符号，弹出栈，
只要弹出栈的开始符号可以匹配每个结束符号，
则括号保持匹配状态。
如果任何时候栈上没有出现符合开始符号的结束符号，
则字符串不匹配


"""

from pythonds.basic.stack import Stack


def parChecker(symbolString):
    s=Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol=symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
                
        index = index + 1
        
    if balanced and s.isEmpty():
        return True
    else:
        return False
    
print(parChecker('(((((())))'))
print(parChecker('((()))'))