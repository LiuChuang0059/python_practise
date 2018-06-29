# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:51:09 2018

@author: lc
"""

class User():
    """ user"""
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.login_attempts=0
    def describe_user(self):
        print(self.first_name,self.age)
    def greetr_user(self):
        print(self.age)
    def increment_login_attempts(self,n):
        self.login_attempts+=n
        print(self.login_attempts)
    def reset_login_attempts(self):
        self.login_attempts=0
liu=User('Liu','Chuang',18)
liu.greetr_user()
liu.increment_login_attempts(1)
liu.increment_login_attempts(3)
liu.reset_login_attempts()
print(liu.login_attempts)
