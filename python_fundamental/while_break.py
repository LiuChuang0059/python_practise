# -*- coding: utf-8 -*-
"""
Created on Sun May 13 17:05:01 2018

@author: dell
"""

prompt="\nEnter some words upper: "
prompt+="\nEnter quit if you want to quit: "
message=''
while message != 'quit':
    message=input(prompt)
    if message != 'quit':
        print(message.upper())
