#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 15:55:56 2018

@author: liuchuang


屏幕处理 

"""


import pyautogui

im = pyautogui.screenshot()  ### im 返回一个image 图像  可以 使用pillow 处理

print(im.getpixel((2,3)))  ## 传入一个元组





