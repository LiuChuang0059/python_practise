# -*- coding: utf-8 -*-
"""
Created on Sun May 13 09:44:09 2018

@author: dell
"""

##放眼世界
W=['Dalian','Shanghai','Hanzhou',"xi'an",'Shenzhen']
print(W)
W1=sorted(W)
print('\n')
print(W1)
print(W)

#反方向临时字符排序
W2=sorted(W,reverse=True)
print('\n')
print(W2)
print(W)

#倒转列表
print('\n')
W.reverse()
print(W)
W.reverse()
print(W)

##永久字母排序
W.sort()
print('\n')
print(W)

#字母反向排序
W.sort(reverse=True)
print(W)



