# -*- coding: utf-8 -*-
"""
Created on Sun May 13 12:21:50 2018

@author: dell
"""

alien_move={'x_position':0,'y_position':0,'speed':'middle'}
alien_move['speed']='slow'
if alien_move['speed'] == 'slow':
    x=1
    y=1
elif alien_move['speed'] == 'middle':
    x=2
    y=2
else:
    x=3
    y=3
alien_move['x_position']=alien_move['x_position']+x
alien_move['y_position']=alien_move['y_position']+y

print(alien_move['x_position'],alien_move['y_position'])