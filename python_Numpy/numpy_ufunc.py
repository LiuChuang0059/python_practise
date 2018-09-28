#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 00:46:16 2018

@author: liuchuang


ufunc是universal function的缩写，
它是一种能对数组的每个元素进行操作的函数。
NumPy内置的许多ufunc函数都是在C语言级别实现的，
因此它们的计算速度非常快。
"""

import numpy as np


x = np.linspace(0,2*np.pi,10)

y=np.sin(x)
###它对x中的每个元素求正弦值，然后将结果返回，并且赋值给y。
###计算之后x中的值并没有改变，而是新创建了一个数组保存结果
##
print(y)


