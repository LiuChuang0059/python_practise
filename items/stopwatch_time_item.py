#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 00:53:43 2018

@author: liuchuang


超级秒表 项目

1.记录从按下回车键开始，每次按键的时间，每次按键都是一个新的“单圈”。 
2.打印圈数、总时间和单圈时间。


这意味着代码将需要完成以下任务:
1.在程序开始时，通过调用 time.time()得到当前时间，将它保存为一个时间戳。 在每个单圈开始时也一样。
2.记录圈数，每次用户按下回车键时加 1。 用时间戳相减，得到计算流逝的时间。
3.处理 KeyboardInterrupt 异常，这样用户可以按 Ctrl-C 退出。
4.打开一个新的文件编辑器窗口，并保存为 stopwatch.py。




创建一个简单的工时表应用程序，当输入一个人的名字时，用当前的时间记录 下他们进入或离开的时间




"""

import time 


# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')

input()
print("Start!")

startTime = time.time()
lastTime = startTime
lapNum =1 


try:
    while True:
        input()
        lapTime =round(time.time()- lastTime,4)
        totalTime = round(time.time()-startTime,4)
        print("Lap %s : total time : %s  lap time: %s" %(lapNum,totalTime,lapTime),end="")
        lapNum+=1
        lastTime = time.time()
        
except KeyboardInterrupt:
    print("\n done")


    
    




    
    
    
