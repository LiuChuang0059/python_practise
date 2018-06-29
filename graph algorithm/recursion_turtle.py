#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 23:57:28 2018

@author: liuchuang




可视化递归

turtle 模块

龟图形



"""

import turtle 


myTurtle = turtle.Turtle()
mywin  = turtle.Screen()  #### 创建一个窗口 


def drawSpiral(myTurtle,linelen):
    if linelen > 0:
        myTurtle.forward(linelen)
        myTurtle.right(120)
        drawSpiral(myTurtle,linelen-5)
        
drawSpiral(myTurtle,100)
mywin.exitonclick()
### 方便的缩小窗口的方法