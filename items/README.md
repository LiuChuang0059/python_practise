# python 小项目练习

# python 小程序
标签 ：python

# 1 Interweaving strings and removing digits
> Your friend Rick is trying to send you a message, but he is concerned that it would get intercepted by his partner. He came up with a solution:
> 1) Add digits in random places within the message.
> 2) Split the resulting message in two. He wrote down every second character on one page, and the remaining ones on another. He then dispatched the two messages separately.
Write a function interweave(s1, s2) that reverses this operation to decode his message!
Example 1: interweave("hlo", "el") -> "hello" Example 2: interweave("h3lo", "el4") -> "hello"
Rick's a bit peculiar about his formats. He would feel ashamed if he found out his message led to extra white spaces hanging around the edges of his message...

* code

```python

def interweave(s1,s2):
    s_1=""
    s_2=""
    out=""
    n=0
    for i in s1:
        if i not in '1234567890':
           t=''.join(i)
           s_1=s_1+t
    n1=len(s_1)
    for j in s2:
        if j not in '1234567890':
           p=''.join(j)
           s_2=s_2+p
    n2=len(s_2)
    #判断长度 但是 有待改进 ： 如果位数差的比较多 while
    if n1==n2:
       pass
    elif n1<n2:
       s_1=s_1+" "
    else:
       s_2=s_2+" "
    
    for i in s_1:
        out = out +i +s_2[n]
        n+=1
    out=out.strip()
    return out
```


------

# 2 count words
```python

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]


print (Counter(words))
Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2, 'not': 1, "don't": 1, "you're": 1, 'under': 1})
print (Counter(words).most_common(4))
[('eyes', 8), ('the', 5), ('look', 4), ('into', 3)]
```

-------

# 3 判断是否完美整数（记录几个大神的）

```python
import math

def is_square(n):
    if n < 0:
        return False
    return (int(math.sqrt(n)) - math.sqrt(n)) == 0
```
```
import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0
```
```
def is_square(n): 
    i=1
    while n>0:
         n=n-i
         i=i+2
  #平方拆成等比数列 
    return n==0
```
------------

# 4 translate 字符转换 删除

```python
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)   # 制作翻译表
 
str = "this is string example....wow!!!"
print (str.translate(trantab))
```

```python
def disemvowel(string):
    return string.translate(None, 'aeiouAEIOU')
```

------------

# 5 循环询问票价

```python

"""
#循环性 咨询票价  直到输入错误数据   可以选择继续 或者 quit
无线循环
输入quit 直接退出程序
###如何控制再开始一段循环 solved
"""


import time

c=0
while c< 10:
    b=True
    while b:
        d=input("Enter your age :  ")#判断输入类型
        if d.isdigit():         #是不是全部是整数
            a=int(d)
            
            if a <=3 :
                print("It's free for you!")
                continue
            elif a>3 and a<12 :
                print("It costs 3$,please!")
                continue
            elif a>=12 and a< 100:
                print("It costs 6$, please!")
                continue
            else:
                b=False  # 超出售票年龄范围
                c+=1
                print('\nError!!!(out of range). Wait for 5s')
                time.sleep(5) # 暂停5秒
        
        elif d!='quit':    #输入有字符 不是quit  报错 继续运行
            print('\nError!!(Enter integer).   Wait for 3s')
            time.sleep(3)
            break
        else:
            break
    
    if d=='quit': #输入quit 退出程序
        print("It is quiting")
        c=1002
    else:
        prompt="\nif you wnat to quit please enter quit:" 
        prompt+="\nif you want to  continue please enter any  key:    "
        e=input(prompt)
        if e =='quit':   #输入有 quit  即时退出程序
            print("It is quiting")
            c=1001

```


--------

## 6 Homework: A byte of python
Checking whether a text is a palindrome should also ignore punctuation, spaces and case. For example, "Rise to vote, sir." is also a palindrome but our current program doesn't say it is. Can you improve the above program to recognize this palindrome?
If you need a hint, the idea is that...1

> Use a tuple (you can find a list of all punctuation marks here) to hold all the forbidden characters, then use the membership test to determine whether a character should be removed or not, i.e. forbidden = (!, ?, ., ...). 


--------
## 7 心形图

```python
grid=[['.','.','.','.','.','.','.'],
      ['.','*','*','.','.','.','.'],
      ['*','*','*','*','.','.','.'],
      ['*','*','*','*','*','.','.'],
      ['.','*','*','*','*','*','.'],
      ['*','*','*','*','*','.','.'],
      ['*','*','*','*','.','.','.'],
      ['.','*','*','.','.','.','.'],
      ['.','.','.','.','.','.','.']]
i=0
while i<7:
    for j in range(0,9):
        print(grid[j][i],end='')
    print('\n')##换行
    i+=1
```


--------
## 8 tic tac toe
[AI_tictactoe](http://inventwithpython.com/chapter10.html)

```python
###建立棋盘空格位置---棋子 现所有位置都是空格
the_board={'1-1':' ','1-2':' ','1-3':' ',
           '2-1':' ','2-2':' ','2-3': '',
           '3-1':' ','3-2':' ','3-3':' ',
           }

###打印棋盘
def print_board(board):
    ###参数为字典
    print(board['1-1']+'|'+board['1-2']+'|'+board['1-3'])
    print('-+-+-')
    print(board['2-1']+'|'+board['2-2']+'|'+board['2-3'])
    print('-+-+-')
    print(board['3-1']+'|'+board['3-2']+'|'+board['3-3'])


### 允许玩家修改棋子
turn='X'
for i in range(9):
    print_board(the_board)
    print('Turn for '+turn)
    move=input(" Move on which space?: ")
    the_board[move]=turn
    if turn == "X":
        turn='O'
    else:
        turn='X'

print_board(the_board)
```
------

## 9 列表物品按数量添加到字典
```python

##展示 物品数目和分类
def display_stuff(stu):
    for k , v in stu.items():
        print(k + ': '+ str(v))
        total_number=0
        total_number+=v
    print("\ntotal_number: " +str(total_number))
    
### 添加物品----添加字典
def add_stuff(st,add_stu):
    for i in add_stu:
        st.setdefault(i,0) ###防止字典里面不含该物品
        st[i]=st[i]+1
    return st      ###注意函数需要返回值
stuff={'rope':1,'arrow':3,'torch':4,'coin':32,'gold':12,'cloth':12}
addstuff=['rope','rope','rope','gold','fish']
stuff_total=add_stuff(stuff,addstuff)
display_stuff(stuff_total)
```

--------

## 10 寻找文本中的 电话号码 email 
```python
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
        (\d{4}|\(\d{4}\))?  ##区号  0101  or (0101) 且不一定必须
        (\s|-|\.)?    ##连接符 0101-1234 or 0101.1234 o1o1 1234 且不一定必须
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

###类似程序：
 1. 寻找网站的URL https://开头
 
 2. 寻找整理日期格式
 
 3. 删除敏感信息 sub()
 
 4. 寻找常见的英文打字错误  如：单词间多个空格 重复单词 多个标点符号

```
------

## 11 记录时间秒表

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 00:53:43 2018
@author: liuchuang
超级秒表 项目
1.记录从按下回车键开始，每次按键的时间，每次按键都是一个新的“单圈”。 
2.打印圈数、总时间和单圈时间。
这意味着代码将需要完成以下任务:
1.在程序开始时，通过调用 time.time()得到当前时间，将它保存为一个时间戳。 在每个单圈开始时也一样。
2.记录圈数，每次用户按下回车键时加 1。 用时间戳相减，得到计算流逝的时间。
3.处理 KeyboardInterrupt 异常，这样用户可以按 Ctrl-C 退出。
4.打开一个新的文件编辑器窗口，并保存为 stopwatch.py。
创建一个简单的工时表应用程序，当输入一个人的名字时，用当前的时间记录 下他们进入或离开的时间
"""

import time 


# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')

input()
print("Start!")

startTime = time.time()
lastTime = startTime
lapNum =1 


try:
    while True:
        input()
        lapTime =round(time.time()- lastTime,4)
        totalTime = round(time.time()-startTime,4)
        print("Lap %s : total time : %s  lap time: %s" %(lapNum,totalTime,lapTime),end="")
        lapNum+=1
        lastTime = time.time()
        
except KeyboardInterrupt:
    print("\n done")
```

--------





