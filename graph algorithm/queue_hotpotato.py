#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 22:07:51 2018

@author: liuchuang



queue  模拟 约瑟夫 问题

我们的程序将输入名称列表和一个称为 num 常量用于报数。
它将返回以 num 为单位重复报数后剩余的最后一个人的姓名

"""


from pythonds.basic.queue import Queue


def hotPotato(namelist,num):
    """
    循环一圈 找出 num人 删除
    
    """
    simqueue = Queue()
    for name in namelist :
        simqueue.enqueue(name)
        
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
            ###  队首删除添加到队尾
            
        simqueue.dequeue()
        ####返回最后 剩余的
        
    return simqueue.dequeue()


namelist = ['a','b','c','d','e','f','g','h','i']
print(hotPotato(namelist,10))

