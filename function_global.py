# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 12:51:23 2018

@author: dell
"""

x = 50


def func():
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)


func()
print('Value of x is', x)