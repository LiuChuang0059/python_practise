# -*- coding: utf-8 -*-
"""
Created on Wed May 30 23:53:23 2018

@author: 刘闯

读写文件
"""

## 创建文件夹
import os 
os.makedirs('C:\\Liu\\Chuang\\o')
###创建多层文件夹


###os.path 模块 ：： 文件名和文件路径

####1 绝对路径 和相对路径
os.path.abspath('.') ##'.'对应着当前路径
os.path.isabs()# 判断是否为绝对路径
os.path.basename('')## 文件名
os.path.dirname('')## 文件路径名
os.path.split('')## t同时获得 文件名和路径的元组 的


###2 查看文件和文件夹 内容 

os.path.getsize('') ###返回文件的字节数
os.listdir('')## 返回路径下的所有文件
###利用个循环 可以计算 路径下所有文件 总字节数

###3 检查路径的有效性
os.path.exists()  ### 检测路径是否存在
os.path.isdir('')###path 存在 并且是一个文件夹
os.path.isfile('')  ### path 存在 并且是一个文件


###4 读写  纯文本文件  .txt .py


###5 用 shelve 模块 保存变量 
import shelve 
shelfFile= shelve.open('mydata')
Men=['Liu','Chuang','chuang'] 
## 类似于字典 有keys  有values 
shelfFile['man']=Men
shelfFile.close()

###6用 pprint.pformat（） 函数保存变量  创建py 文件
import pprint
cats=[{'name':'Liu','Age':'16'},{'name':'Chuang','age':'12'}]
fileCat=open('mycat.py','w')
fileCat.write('cats =' + pprint.pformat(cats) + '\n')## pprint 返回字符串
fileCat.close()

###导入python 脚本
import mycat
mycat.cats
mycat.cats[0]
### 只有基本数据类型 整形 浮点型 字符串 列表 字典 作为简单文本写入



 





