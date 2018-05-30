# -*- coding: utf-8 -*-
"""
Created on Sun May 20 22:38:22 2018

@author: 刘闯

修改剪切板内容 重新粘贴


"""

import pyperclip

text= pyperclip.paste()
#返回剪切板上的所有文本 返回一个 长的字符串
print(text+'#')

#切割字符串 以/n W为标志 得到列表 
lines=text.split('\n')
for i in range(len(lines)):
    lines[i]='* '+lines[i]
text='\n'.join(lines)
pyperclip.copy(text)  #改变剪切板内容
print(text)