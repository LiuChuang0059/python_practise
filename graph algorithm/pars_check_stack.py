#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 22:38:04 2018

@author: liuchuang





检查确保它正确匹配栈顶部开始符号的类型。
如果两个符号不匹配，则字符串不匹配。
如果整个字符串都被处理完并且没有什么留在栈中，
则字符串匹配。
"""


from pythonds.basic.stack import Stack


def parChecker(symbolString):
    s=Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol=symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top=s.pop()
                if not match(top,symbol):
                    balanced = False
                
        index = index + 1
        
    if balanced and s.isEmpty():
        return True
    else:
        return False
def match(left,right):
    lefts = '([{'
    rights= ')]}'
    return lefts.index(left) == rights.index(right)

print(parChecker("({{{[]}}})"))
print(parChecker("({])"))