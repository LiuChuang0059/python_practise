# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:11:33 2018

@author: 刘闯

提取 电话号码和 Email地址


1.从剪切板获取文本：
  1-1pyperclip
2.找出其中的 电话号码 和Email 地址：
   2-1 两个正则表达式
   2-2 找出所有的匹配
   2-3 放入字符串
   2-4 如果没有匹配 ；；；
   
3. 粘贴到剪切板

"""

import  pyperclip, re
text=str(pyperclip.paste())

# phone 010-8888-8888
phonenumber_regex=re.compile(r'''(
        (\d{4}|\(\d{4}\))?  ##区号  0101  or (0110) 且不一定必须
        (\s|-|\.)?    ##连接符 0101-1234 or 0101.1234 0101 1234 且不一定必须
        (\d{4})
        (\s|-|\.)?  
        (\d{4})
        )''',re.VERBOSE)


## email  ex: 1659608216@qq.com
email_regex=re.compile(r'''(
        [a-zA-Z0-9._%+-]+    # username
        @         
        [a-zA-z0-9-]+        #domin name
        (\.[a-zA-Z]{2,})+  #.cn or.com  (.edu.cn)
        )''',re.VERBOSE)

###findall 抓取信息 tuple--list
matches=[]
for groups in phonenumber_regex.findall(text):
    phonenumber='-'.join([groups[1],groups[3],groups[5]])
    matches.append(phonenumber)
for groups in email_regex.findall(text):
    matches.append(groups[0])


####copy to clipboard
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard:")
    print('\n'.join(matches))
else:
    print('No number or email found')

###问题  电话号码和 手机号码 冲突显示 需要个判断（开头）
#### 校园邮箱 识别 缺失   solved
#### 随机8位数字 都添加识别   错误

#### 识别 3位  是数字还是电话号 
    
    
    













































