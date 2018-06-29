#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 00:50:33 2018

@author: liuchuang
"""
import numpy as np



a= np.array([1,2,3])## 一位数组
print(type(a))
print(a.shape)  ###数组大小
print(a[0])

a[0]=5
print(a)


b=np.array([[1,2,3],[4,5,6]]) ##二维数组
print(b.shape)
print(b[0,1],b[1,1])
print(b)

print('\n\n' )

c=np.zeros((2,2))
print(c)
print('\n')

d=np.ones((1,2))
print(d)
print('\n')


e=np.full((3,3),7)
print(e)
print('\n')

f =np.eye(2)
print(f)
print('\n')


g=np.random.random((2,2))
print(e)


h=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

#use slicing to pull out subarray

k=h[:2,1:3]



h.shape=4,3
h.shape=2,-1### -1 时自动计算轴的长度

l=h.reshape((6,2))##数组l,h 共享数据储存内存区域
print(l)




print(h)
print('\n\n')

print(k)


####????
row_r1 = h[1, :]    # Rank 1 view of the second row of a
row_r2 = h[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"

# We can make the same distinction when accessing columns of an array:
col_r1 = h[:, 1]
col_r2 = h[:, 1:2]
print(col_r1, col_r1.shape)  # Prints "[ 2  6 10] (3,)"
print(col_r2, col_r2.shape)




### 数组的元素类型

array_type=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]],dtype=np.float)

print(array_type)

array_type2=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]],dtype=np.complex)
print(array_type2)


###  创建数组的元素
 
#### 1 arange  ===range   (开始，终止 ，步长)
array1 = np.arange(0,1,0.1)
print(array1)


#### 2 linespace  （开始，终止，元素个数）默认包含终止值（endpoint）
array2 = np.linspace(0,1,10)
print(array2)


#### 3 logspace  等比
array3 = np.logspace(0,3,33)
print(array3)


### 字节序列创建数组
s = "abcdefgh"


#### 1 字符串为字节序列，每个字符占一个字节
s_int8 = np.fromstring(s,dtype = np.int8)

#### 2 16bit 两个相邻字节为一个整数
s_int16 = np.fromstring(s,dtype = np.int16)

#### 3 64位 双精度浮点数数组
s_float = np.fromstring(s, dtype = np.float)
 

print(s_int8,s_int16,s_float)


### 二维数组创建乘法表
def func(i,j):
    return (i+1)*(j+1)

a = np.fromfunction(func,(9,9))
### 第一个参数 为计算每个数组元素的函数，，
### 第二个参数 序列 数组大小

print(a)





























