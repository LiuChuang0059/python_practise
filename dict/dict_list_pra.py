# -*- coding: utf-8 -*-
"""
Created on Sat May 19 11:12:37 2018

@author: 刘闯

记录游戏物品数量

"""

"""

##展示 物品数目和分类
def display_stuff(stuf):
    for s,n in stuf.items():
        print(s + ': '+ str(n))
        total_number=0
        total_number+=n
    print("\ntotal_number: " +str(total_number))
stuff={'rope':1,'arrow':3,'torch':4,'coin':32,'gold':12,'cloth':12}
display_stuff(stuff)
### 添加物品----添加字典

def add_stuff(st,add_stu):
    for k,v in add_stu.items():
        st.setdefault(k,v)
        st[k]=st[k]+add_stu[k]
stuff={'rope':1,'arrow':3,'torch':4,'coin':32,'gold':12,'cloth':12}
addstuff={'shoe':23,'rope':21}
stuff_total=add_stuff(stuff,addstuff)
display_stuff(stuff_total)
"""


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