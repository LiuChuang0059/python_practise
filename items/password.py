# -*- coding: utf-8 -*-
"""
Created on Sun May 20 19:30:38 2018

@author: 刘闯

口令保管箱
"""

###账号的名称和密码
passwords={'Email':'asdfghjkl1234',
           'QQ':'1234567899asdfgh',
           'Wechat':'3ertyhvgjihhh'}


##处理命令行参数
##命令行参数储存在sys.argv

import sys  ##命令行参数
import pyperclip


if len(sys.argv)<2:
    print('Usage: python pw.py [acount] - copy account password')
    sys.exit()
account=sys.argv[1]
###第一个命令行参数是账户名称

####复制正确的口令
if account in passwords.keys():
    pyperclip.copy(passwords[account])
    print('password for ' + account + ' copied to clipboard.')
else:
    print("There is no account named " + account )
    