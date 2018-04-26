# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 23:56:20 2018

@author: dell
"""

def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [x + y for x, y in zip(L[:-1], L[1:])] + [1]
        
    
    
    
#生成器
        