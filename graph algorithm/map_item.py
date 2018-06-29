#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 18:14:12 2018

@author: liuchuang


"""

import webbrowser,sys, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    
else:
    address = pyperclip.paste()
    

webbrowser.open('http://www.google.com/maps/place/' + address)