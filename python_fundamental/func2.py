# -*- coding: utf-8 -*-
"""
Created on Mon May 14 20:49:33 2018

@author: lc

输入制衣  判断 无输入 或不在范围内  默认值
询问 是否按照默认值执行
"""


def make_shirt(size='Xl',pattern='I love you'):
    print("\nMy shirt is " +  size.upper() +" and with a " + pattern)
    
A=input("Which size?:  ")
B=input("which pattern? :")
L1=['s','m','l','xl','xxl']
L2=['pig','dog','cat','panda']
if A in L1 and B in L2 :
    make_shirt(A,B)
elif A not in L1 and B in L2 :
    make_shirt(pattern=B)
elif A in L1 and B not in L2 :
    make_shirt(size=A)
else:
    print("Sorry!! we don't have ")
    C=input("would you want to print by default(y/n):  ")
    if C=='y':
        make_shirt()
    

