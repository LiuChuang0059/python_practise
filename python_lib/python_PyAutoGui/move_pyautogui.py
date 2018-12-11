#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 00:04:39 2018

@author: liuchuang

控制鼠标移动
"""
import pyautogui


### 1 移动鼠标
for i in range(10):
    pyautogui.moveTo(100,100,duration=1.0)###移动到指定的像素点
    pyautogui.moveTo(150,200,duration=1.0)
    pyautogui.moveTo(250,100,duration=1.0)
    
    
for i in range(10):
    pyautogui.moveRel(1000,0,duration=0.25) ### 移动多少像素点
    pyautogui.moveRel(0,800,duration=0.25)
    pyautogui.moveRel(-1000,0,duration=0.25)
    pyautogui.moveRel(0,-800,duration=0.25)
    
    
### 2 获取鼠标位置

a=pyautogui.position()  ##返回鼠标位置元祖
