# -*- coding: utf-8 -*-
"""
Created on Mon May 14 21:05:28 2018

@author: lc

创建一个描述音乐专辑的 字典 包含 歌手名 专辑名 歌曲数
"""
def make_album(singer_name,album_name,number=""):
    album={}
    album['singer_name']=singer_name
    album['album_name']=album_name
    if number :
        album['number']=number
    return album
A=make_album('Li','Shanqiu',10)
B=make_album('Luo','Lianqu')
print(A,B)

C=input('singer_name:')
D=input('album_name: ')
E=input('number:   ')

F=make_album(C,D,E)
print(F)
