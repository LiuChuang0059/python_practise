#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 21:42:37 2018

@author: liuchuang


列表 实现队列


"""

class Queue():
    """
    假定 队尾在列表的位置为0 
    删除队首 即是 列表的最后一个元素
    
    """
    
    
    
    def __init__(self):
        self.items = []
    
    
    def isEmpty(self):
        return self.items == []
    
    
    def enqueue(self,item):
        self.items.insert(0,item)
        #### 列表0的位置插入  元素
        
    def dequeue(self):
        return self.items.pop()
    
    
    def size(self):
        return len(self.items)
    
    

q=['2','3','4']
q = Queue()

print(q.isEmpty())
 

q.enqueue(34)

q.enqueue('23')

print('\n')
print(q.size())




































