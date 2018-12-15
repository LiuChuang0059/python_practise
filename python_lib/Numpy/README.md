# numpy 学习




## 1 内存结构

![](http://old.sebug.net/paper/books/scipydoc/_images/numpy_memory_struct.png)

```python
    a = np.array([[0,1,2],[3,4,5],[6,7,8]], dtype=np.float32)
```


> strides中保存的是当每个轴的下标增加1时，数据存储区中的指针所增加的字节数。例如图中的strides为12,4，即第0轴的下标增加1时，数据的地址增加12个字节：即a[1,0]的地址比a[0,0]的地址要高12个字节，正好是3个单精度浮点数的总字节数；第1轴下标增加1时，数据的地址增加4个字节，正好是单精度浮点数的字节数。
>
> 如果strides中的数值正好和对应轴所占据的字节数相同的话，那么数据在内存中是连续存储的。然而数据并不一定都是连续储存的


## 2 ufunc
* func是universal function的缩写，它是一种能对数组的每个元素进行操作的函数。NumPy内置的许多ufunc函数都是在C语言级别实现的，因此它们的计算速度非常快。


```python

import numpy as np


x = np.linspace(0,2*np.pi,10)

y=np.sin(x)
###它对x中的每个元素求正弦值，然后将结果返回，并且赋值给y。
###计算之后x中的值并没有改变，而是新创建了一个数组保存结果

print(y)

```

* y = x1 + x2:	add(x1, x2 [, y])

* y = x1 - x2:	subtract(x1, x2 [, y])

* y = x1 * x2:	multiply (x1, x2 [, y])

* y = x1 / x2:	divide (x1, x2 [, y]), 如果两个数组的元素为整数，那么用整数除法

* y = x1 / x2:	true divide (x1, x2 [, y]), 总是返回精确的商

* y = x1 // x2:	floor divide (x1, x2 [, y]), 总是对返回值取整

* y = -x:	negative(x [,y])

* y = x1**x2:	power(x1, x2 [, y])

* y = x1 % x2:	remainder(x1, x2 [, y]), mod(x1, x2, [, y])

------
 数组对象支持这些操作符，极大地简化了算式的编写，不过要注意如果你的算式很复杂，并且要运算的数组很大的话，会因为产生大量的中间结果而降低程序的运算效率。例如：假设a b c三个数组采用算式x=a*b+c计算，那么它相当于:

-----

```python
t = a * b
x = t + c
del t
# 也就是说需要产生一个数组t保存乘法的计算结果，然后再产生最后的结果数组x。我们可以通过手工将一个算式分解为x = a*b; x += c，以减少一次内存分配。
```


------------

## 3 保存

### 1 通过下标范围产生数组  和原数组共享数据空间
```python
b=a[::-1]  ## 步长为负数 倒序
c=a[3:7]   ### 左开右闭
```

### 2 通过整数序列 元素选取 每个元素作为下标  获得新数组 不共享空间
```python
d=a[[1,2,3,5]]
a[[1,2,3]]=4,5,6


print(a,b,c,d)

```
### 3 布尔数组

```python
e = np.arange(3)
f=e[np.array([True,False,True])]
print('\n\n')
print(f)

```
--------
--------

## 4.  arrange

1. np.arrange --numpy.arange([start, ]stop, [step, ]dtype=None)  : 每步分割的大小

> Values are generated within the half-open interval [start, stop)

```python

>>> np.arange(3)
array([0, 1, 2])
>>> np.arange(3.0)
array([ 0.,  1.,  2.])
>>> np.arange(3,7)
array([3, 4, 5, 6])
>>> np.arange(3,7,2)
array([3, 5])

```


-----


2. numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)

* endpoint ： 是否包含 stop 值， 不过 总数 num  不变

* retstep : 给出 步长 If True, return (samples, step)

```python
>>> np.linspace(2.0, 3.0, num=5)
array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ])
>>> np.linspace(2.0, 3.0, num=5, endpoint=False)
array([ 2. ,  2.2,  2.4,  2.6,  2.8])
>>> np.linspace(2.0, 3.0, num=5, retstep=True)
(array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25

```

-----

3. np.meshgrid


```python
nx, ny = (3, 2)
>>> x = np.linspace(0, 1, nx)
>>> y = np.linspace(0, 1, ny)
>>> xv, yv = np.meshgrid(x, y)
>>> xv
array([[ 0. ,  0.5,  1. ],
       [ 0. ,  0.5,  1. ]])
>>> yv
array([[ 0.,  0.,  0.],
       [ 1.,  1.,  1.]])

```


* size(x) = 3  理解为坐标轴的x ---对应的 矩阵的列。， 相当于 坐标轴上的一条条横线； size(y) = 2 理解为坐标轴 的y。  对应矩阵的 row； 相当于 坐标轴上一列列竖线

* 二者 均需 broadcast  到相应的行数 和列数


* xv yv  矩阵 坐标数相同的点 ，共同表示 坐标轴内的 一个点。例如 x0y0 = (0,0) ;x0y1 = (0,1)


**Meshgrid函数常用的场景有等高线绘制及机器学习中SVC超平面的绘制**




---

## 5.

* np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等，类似于pandas中的concat()。
* np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等，类似于pandas中的merge()。
















