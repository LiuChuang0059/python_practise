#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 17:16:29 2018

@author: liuchuang


键盘控制


"""

import pyautogui


pyautogui.click(pyautogui.position())  ###获取鼠标位置 并点击


pyautogui.typewrite('hello world',0.1)  ##打字  第二个参数为打字速度

pyautogui.typewrite(['h','enter','\n','w'])  ###列表表示键盘上的键值


### 1 按下 键

pyautogui.keyDown('shift')
pyautogui.press('5')  ## press = up + down
pyautogui.keyUp('shift')


### r热键组合  
pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('ctrl')
pyautogui.keyUp('c')


pyautogui.hotkey('ctrl','c')

