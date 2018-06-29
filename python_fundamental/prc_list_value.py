# -*- coding: utf-8 -*-
"""
Created on Sun May 13 10:26:26 2018

@author: dell
"""

##列表解析
A=list(range(1,20,2))
for odd in A:
    print(odd)
print([odd for odd in range(0,20,2)])

##3的倍数
B=[]
for value in range(3,30):
    if value%3==0:
        B.append(value)
print(B)

##cubic
print([c**3 for c in range(1,10)])

