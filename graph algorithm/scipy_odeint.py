#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 13:05:24 2018

@author: liuchuang
"""

from scipy.integrate import odeint 
import numpy as np 

def lorenz(w, t, p, r, b): 
    # 给出位置矢量w，和三个参数p, r, b计算出
    # dx/dt, dy/dt, dz/dt的值
    x, y, z = w
    # 直接与lorenz的计算公式对应 
    return np.array([p*(y-x), x*(r-z)-y, x*y-b*z]) 

t = np.arange(0, 30, 0.01) # 创建时间点 
# 调用ode对lorenz进行求解, 用两个不同的初始值 

"""

lorenz， 它是计算某个位移上的各个方向的速度(位移的微分)
(0.0, 1.0, 0.0)，位移初始值。计算常微分方程所需的各个变量的初始值
t， 表示时间的数组，odeint对于此数组中的每个时间点进行求解，得出所有时间点的位置
args， 这些参数直接传递给lorenz函数，因此它们都是常量
"""
track1 = odeint(lorenz, (0.0, 1.00, 0.0), t, args=(10.0, 28.0, 3.0)) 
track2 = odeint(lorenz, (0.0, 1.08, 0.0), t, args=(10.0, 28.0, 3.0)) 

# 绘图
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 

fig = plt.figure()
ax = Axes3D(fig)
ax.plot(track1[:,0], track1[:,1], track1[:,2])
ax.plot(track2[:,0], track2[:,1], track2[:,2])
plt.show()