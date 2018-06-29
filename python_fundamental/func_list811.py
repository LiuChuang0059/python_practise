# -*- coding: utf-8 -*-
"""
Created on Mon May 14 21:49:13 2018

@author: lc

函数和列表

"""

magicians=['Liu','Chuang','zou','xiao']
def make_great(lists):
    for list in lists :
        list='the Great '+ list # 修改列表
        print(list)


#传递副本
make_great(magicians[:])
print(magicians)
