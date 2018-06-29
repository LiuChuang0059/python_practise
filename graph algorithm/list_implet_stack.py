#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 01:06:29 2018

@author: liuchuang


列表实现栈

"""

class Stack:
    '''
    栈的操作 类
    '''
    def __init__(self):
        ###
        self.items = []
    
    
    def isEmpty(self):
        ###判断是否为空栈 返回布尔值
        return self.items == []
    
    
    def push(self,item):
        ## 压入 元素 添加到队尾
        self.items.append(item)
        
    
    def pop(self):
        ###从队尾删除
        return self.items.pop()
    
    
    def peek(self):
        ###返回栈顶部值
        return self.items[len(self.items)-1]
    
    
    def size(self):
        ###栈的大小
        return len(self.items)


from pythonds.basic.stack import Stack

### 实例化 
s=Stack()
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
