# -*- coding: utf-8 -*-
"""
Created on Tue May 15 00:41:17 2018

@author: lc
创建一个类 包含属性方法

"""


class User():
    """ user"""
    def __init__(self,first_name,last_name,age,weight):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.weight=weight
    def describe_user(self):
        print(self.first_name,self.age)
    def greetr_user(self):
        print(self.age)
liu=User('Liu','Chuang',18,76)
liu.greetr_user()