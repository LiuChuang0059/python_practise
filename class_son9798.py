# -*- coding: utf-8 -*-
"""
Created on Tue May 15 13:12:48 2018

@author: lc

继承子类

"""

"""
class User():
     ###userkk
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

class Admin(User):
    def __init__(self,first_name,last_name,age):####错误太难找两个下划线
        super().__init__(first_name,last_name,age)
        self.p=["can add post","can delete post","can ban user"]
    def show_privileges(self):
        for i in self.p:
            print(i)
liu=Admin('Liu','Chuang',20)
liu.increment_login_attempts(2)
liu.show_privileges()
"""

###创建子类 打印权限
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

class Show_privileges():
    def __init__(self):
        self.p=["can add post","can delete post","can ban user"]
    def show_privileges(self):
        for i in self.p:
            print(i)
class Admin(User):
    def __init__(self,first_name,last_name,age):####错误太难找两个下划线
        super().__init__(first_name,last_name,age)
        self.show=Show_privileges()

        