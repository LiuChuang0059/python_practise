#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 00:23:51 2018

@author: liuchuang


链表实现 无序列表

每一项 保留下一项的位置
"""
class Node:
    """
    链表的基本 是 节点  
    每个节点 包含列表项本身   以及下一个 节点的引用
    """
    
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        
    def getData(self):
        return self.data
    
    
    def getNext(self):
        return self.next
    
    def setData(self,newdata):
        self.data = newdata
        
    def setNext(self,newnext):
        self.next = newnext




class UnorderedList:
    """
    每个节点通过显式引用链接到下一个节点
    第一个节点（包含第一个项）
    UnorderedList 类必须保持对第一个节点的引用
    """
    
    
    def __init__(self):
        self.head = None
        
    
    def isEmpty(self):
        ###检查链表头是否是 None 的引用
        return self.head == None
    
    
    def add(self,item):
        temp = Node(item)## 创建一个新的结点
        temp.setNext(self.head)  ###新结点 连在旧的第一个
        self.head = temp  ### 头 引用 新的结点
        
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count +1
            current = current.getNext()     
        return count
        
    def search(self,item):
        current = self.head
        found = False
        while not found and current != None :
            #### 两个条件  ： 有下一个值； 值 不是要寻找的
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    
    def remove(self,item):
        current = self.head 
        previous = None
        found = False
        
        while not found :   
            ### 搜索  假设 删除项存在
            if current.getData() == item :
                found = True
            else:
                previous =  current  ###pre 在 current 前一个节点
                current = current.getNext()
        
        if previous == None : ### 删除项 为列表第一项
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
                
        
mylist = UnorderedList()
mylist.add(12)
mylist.add(13)
mylist.add(14)


print(mylist.size())
print(mylist.search(12),mylist.search(15))

mylist.remove(13)
print(mylist.search(13))


### 链表类本身不包含任何节点对象。
###它只包含对链接结构中第一个节点的单个引用