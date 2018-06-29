# -*- coding: utf-8 -*-
"""
Created on Sun May 13 01:11:09 2018

@author: dell
"""
list=['L','C','Z','X','W']
print(list)
print("w is not intended")
list.remove('W')  #移除一个嘉宾
list.append('w') #增补一个嘉宾
print(list)

#修改名单
list.insert(0,'chuang')
n=len(list)
if n%2==1:
    list.insert((n-1/2),'xiao')
else:
    list.insert(int((n/2)),'xiao')
list.append('wei')
print(list)

#每一位嘉宾发出邀请
for i in list:
    print("invite  "+ i.title() + ' to my party')#每一位嘉宾发出邀请
print('\nSorry,only two people i can invite')


#删除只剩两位
n=len(list)
while n >2:
    l=list.pop()
    print(l + " I am sorry")##如果不用L替换  list.pop会再删除一个 隔着删除
    n=len(list)
print(list)
for i in list:
    print("invite  "+ i.title() + ' to my party')#剩下两位嘉宾发出邀请

#清空名单
del list[::]
if len(list)==0:
    print('名单清空')
else:
    print("no")
