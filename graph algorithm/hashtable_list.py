#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 23:40:59 2018

@author: liuchuang


两个列表 实现 一个 HashTable

一个保存 key 值
一个保存 value值

"""

class HashTable:
    """
    hash 函数为余数  除法hash
    冲突解决方法 +1 后 rehash  重新探测
    """
    
    def __init__(self):
        self.size = 5 ###hash 初始的大小
        self.slots = [None] * self.size ## 11个空位置
        self.data = [None] * self.size
        
        
    def put(self,key,value):
        """
        插入key--value
        """
        hashvalue = self.hashfunction(key,len(self.slots))
        ##计算hash值
        
        if self.slots[hashvalue] == None:
            ###如果哈希值为对应key列表的位置为空
            self.slots[hashvalue] = key ## 直接插入
            self.data[hashvalue] = value
        
        else: 
            ###如果已经存在数值
            if self.slots[hashvalue] == key: 
                ###如果key 已经存在 在self.slots??
                self.data[hashvalue] = value
            ### 新的值替换
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                ###rehash  向下排一位
                while self.slots[nextslot] != None and \
                      self.slots[nextslot] !=key:
                          nextslot = self.rehash(nextslot,len(self.slots))
                
                
                
                if self.slots[nextslot] == None:
                    self.slots[nextslot] =key
                    self.data[nextslot] = value
                    
                else:
                    self.data[nextslot] = value
    
    
    def hashfunction(self,key,size):
        return key % size
    
    
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
    
    
    
    def get(self,key):
        """
        查找key值 
        """        
        startslot = self.hashfunction(key,len(self.slots))
        
        
        data = None
        stop = False
        found = False
        
        position = startslot
        
        
        while self.slots[position] != None and not stop and not found:
            
            if self.slots[position] == key:
                found = True
                data= self.data[position]
            
            else:
                ##调用rehash 定位下一个位置
                position = self.rehash(position,len(self.slots))
                
                if position == startslot:
                    ### 返回到初始槽 用尽所有槽
                    stop = True
        
        return data
    
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,data):
        self.put(key,data)
        
        
        
H = HashTable()

H[1]="A"
H[2]="B"
H[3]="C"
H[4]="D"
H[5]="E"
H[1]="a"

print(H.data)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        