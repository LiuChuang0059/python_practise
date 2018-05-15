# -*- coding: utf-8 -*-
"""
Created on Mon May 14 00:04:16 2018

@author: dell
"""

prompt="\nEnter some words upper: "
prompt+="\nEnter quit if you want to quit: "

act=True
while act :
    message=input(prompt)
    if message == 'quit':
        act=False
    elif message == 'QUIT':
        act=False
    else:
        print(message)
        