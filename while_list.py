# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:33:33 2018

@author: lc

使用while  搬运列表信息
将未验证的用户运到已经验证的
订单---未完成订单

while 删除列表信息 （列表很多重复信息）


"""

un_users=["A","B","C","D"]
users=[]

while un_users:
    in_users=un_users.pop()
    print(in_users + '  is  joining')
    users.append(in_users)
for user in users :
    print(user)
print(un_users,users)

#while 删除列表信息 （列表很多重复信息）
pets=['A','B','C','D','A','D','F','A']
while 'A' in pets:
    pets.remove('A')
print(pets)