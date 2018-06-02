# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 00:55:09 2018

@author: 刘闯

组织文件


"""

"""
###1 shutil 模块

####1 复制文件和文件夹
import os,shutil


os.chdir('C:\\') ## 更爱当前目录
shutil.copy('sourse','destination')  #！！！ 返回一个字符串 被复制文件的路径
### 如果 destination 是一个文件名  ，复制文件的新名字  否则 原名

shutil.copytree("c:\\a","c:\\a_backup") ###复制整个文件夹 以及他包括的文件以及文件夹
### 相当于备份 a


####2 文件和文件夹的移动
shutil.move('sourse','destination')
####1 des为文件夹 则文件 移入文件夹 保存原有的文件名 ！！！ 很可能和源文件冲突覆盖
####2 des 为文件名  则将文件移动到文件夹并且 更改名字
shutil.move("C:\\bacon.txt","C:\\eggs\\new_bacon.txt")

####3 如果目录下没有文件夹 所以假定des指定的是一个文件而不是文件夹，
bacon.txt ##文本文件改名为 eggs 无扩展名


####3 永久删除文件和文件夹
os.unlink(path)## 删除路径的文件
os.rmdir(path)## 删除路径的空文件夹
os.rmtree(path) ## 删除文件夹以及其包含的所有文件和文件夹

####4 文件删除到 回收站 ： send2trash
import send2trash
send2trash.send2trash("")


###2 遍历目录树：  处理文件夹中的每一个文件
import os 
for folderName,subfolders,filenames in os.walk("C:\\"):
    print(folderName)
os.walk()###返回三个值 1 当前文件夹的字符串 2 当前文件夹的子文件夹 字符串列表 3 当前文件夹的文件字符串列表
"""


###3 zipfile模块 压缩 文件
####1 读取 ZIP文件
import zipfile ,os
os.chdir(r'C:\Users\dell\Desktop\summer_camp\LAMDA')
liuzip=zipfile.ZipFile('Liu.zip')
names=liuzip.namelist()
for name in names:
    print(name.decode('utf-8'))###?如何打印中文 待解决
    
LiuInfo=liuzip.getinfo('spam.txt')
LiuInfo.file_size
LiuInfo.compress_size

    


"""
import os

inpath = 'G:\Android\MyAndroid\UI设计'
uipath = unicode(inpath,"utf-8")  ##对路径进行utf-8编码

list = os.listdir(uipath)   ##获得文件目录列表

for each in list:   ##遍历list列表
   print(each.encode('utf-8'))   ##将该目录下文件名全部打印出来


import codecs 
f = codecs.open('text.text','r+',encoding='utf-8')#必须事先知道文件的编码格式，这里文件编码是使用的utf-8 
content = f.read()#如果open时使用的encoding和文件本身的encoding不一致的话，那么这里将将会产生错误 
f.write('你想要写入的信息') 
f.close()

import chardet  
  
  
# 获取文件编码类型  
def get_encoding(file):  
    # 二进制方式读取，获取字节数据，检测类型  
    with open(file, 'rb') as f:  
        return chardet.detect(f.read())['encoding']  
  
  
file_name = 'my.ini'  
encoding = get_encoding(file_name)  
print(encoding)
"""
#####2 从zip中解压缩
liuzip.extractall('A')  # 全部解压  可以传入一个文件夹名称  解压缩到 文件夹目录 
liuzip.extract('B.txt',A)## 单个解压到指定目录

#####3 创建压缩文件
import zipfile
new_zip=zipfile.ZipFile('new.zip','w')
new_zip.write('spam.txt',compress_type=zipfile.ZIP_DEALATED)##'w'写入会擦除原有内容 ‘a’添加
new_zip.close()



