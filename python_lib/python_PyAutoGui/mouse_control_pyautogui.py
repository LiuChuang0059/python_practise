#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 11:09:02 2018

@author: liuchuang


控制鼠标交互
"""

import pyautogui as pg
import time

"""
###1 点击鼠标  click = mouseDown + mouseUp

pg.click(700,850,button='left')
"""
##pyauotgui.doubleClick() 双击左键
##pyautogui.rightClick()  双击右键
## pyautogui.middleClick()  双击中间



### 2 拖动鼠标  dragTo()  dragRel()
time.sleep(5) ###延迟5s  便于切换窗口
pg.click()   ###确定画图 软件窗口置前
distance = 200
while distance > 0:
    pg.dragRel(distance,0,duration=0.2)
    distance = distance -5 
    pg.dragRel(0,distance,duration=0.2)
    pg.dragRel(-distance,0,duration=0.2)
    distance = distance - 5
    pg.dragRel(0,-distance,duration=0.2)
    
    
### 3 窗口滚动 

pg.scroll(100)  ## + :up  - : down

