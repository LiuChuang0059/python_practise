#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 00:39:04 2018

@author: liuchuang


time.sleep  function

如果需要让程序暂停一下，就调用 time.sleep()函数，并传入希望程序暂停的秒
"""

import time 

for i in range(3):
    print("I")
    time.sleep(2)
    print("Love")
    time.sleep(2)
    print("You")
    time.sleep(2)

