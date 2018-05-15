# -*- coding: utf-8 -*-
"""
Created on Mon May 14 00:15:01 2018

@author: dell



#循环性 咨询票价  直到输入错误数据   可以选择继续 或者 quit
无线循环
输入quit 直接退出程序
###如何控制再开始一段循环 solved
"""


import time

c=0
while c< 10:
    b=True
    while b:
        d=input("Enter your age :  ")#判断输入类型
        if d.isdigit():         #是不是全部是整数
            a=int(d)
            
            if a <=3 :
                print("It's free for you!")
                continue
            elif a>3 and a<12 :
                print("It costs 3$,please!")
                continue
            elif a>=12 and a< 100:
                print("It costs 6$, please!")
                continue
            else:
                b=False  # 超出售票年龄范围
                c+=1
                print('\nError!!!(out of range). Wait for 5s')
                time.sleep(5) # 暂停5秒
        
        elif d!='quit':    #输入有字符 不是quit  报错 继续运行
            print('\nError!!(Enter integer).   Wait for 3s')
            time.sleep(3)
            break
        else:
            break
    
    if d=='quit': #输入quit 退出程序
        print("It is quiting")
        c=1002
    else:
        prompt="\nif you wnat to quit please enter quit:" 
        prompt+="\nif you want to  continue please enter any  key:    "
        e=input(prompt)
        if e =='quit':   #输入有 quit  即时退出程序
            print("It is quiting")
            c=1001
        
'''
该程序有操作次数限制
如何控制无限次  solved
'''      
