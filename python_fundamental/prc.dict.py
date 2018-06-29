# -*- coding: utf-8 -*-
"""
Created on Sun May 13 12:57:43 2018

@author: dell
"""

favor_lan={
        'a':'py',
        'b':'c+',
        'c':'java',
        'd':'R',
        }
favor_lan2={
        'a':'py',
        'b':'c+',
        'c':'java',
        'd':'R',
        'e':'fortrun',
        'f':'javascript',
        }
for name in favor_lan2.keys():
    if name in favor_lan.keys():
        print('Thank  ' + name.title() +'  for intending')
    else:
        print('please  ' + name.title() + '  intend')
