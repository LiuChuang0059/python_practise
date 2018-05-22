# -*- coding: utf-8 -*-
"""
Created on Sun May 13 15:31:19 2018

@author: dell
"""


    
 #批量外星人   

aliens=[]
for i in range(1,10):
    alien1={'color':'green','point':5}###不能放在for外面
    aliens.append(alien1)

#批量修改外星人
for alien in aliens[:1]:
    if alien['color']== 'green':
        alien['color']='blue'
        alien['point']= 2
    elif alien['color']=='red':
        alien['color']='xxx'
        alien['point']= 21
for alien in aliens[0:6]:
    print(alien)
    
        