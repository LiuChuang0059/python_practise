# -*- coding: utf-8 -*-
"""
Created on Mon May 21 23:54:58 2018

@author: 刘闯

文本模式查找

"""
###查找一个12位的电话号码 例： 123-456-7890
def is_phonenumber(text):
    # 逐位判断
    if len(text)!=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print(is_phonenumber('123-456-7890'))
print(is_phonenumber('123-456-789u'))

###########在多于12位的文本中查找
def find_text(message):
    for i in range(len(message)):
        message_temporary=message[i:i+12]
        if is_phonenumber(message_temporary):
            print("phone number: " + message_temporary)
    print('Done')

########只能查找固定模式的文本
    ###代码运行较慢  O(n)





m='123-456-7890 for a ment aline libe lieb 098-654-3222  for a moment 1234-123-123'
find_text(m)





