# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 09:43:18 2018

@author: dell
"""

class SchoolMember:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("innitialing {}".format(self.name))
        
    def tell(self):
        print("Name: {}   Age: {:d} ".format(self.name,self.age),end=" ")
       
        '''
        The end parameter is used in
        the print function in the superclass's 
        tell() method to print a line and allow the 
        next print to continue on the same line. 
        This is a trick to make print not print a \n (newline) symbol 
        at the end of the printing.
        '''
        
class Teacher:
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print("innitial: {}".format(self.name))
    
    
    def tell(self):
        SchoolMember.tell(self)
        print("Salary : {}".format(self.salary))
        
        
class Student:
    def __init__(self,name,age,mark):
        SchoolMember.__init__(self,name,age)
        self.mark=mark
        print("innitial: {}".format(self.name))
    
    
    def tell(self):
        SchoolMember.tell(self)
        print("Mark : {}".format(self.mark))
        
T=Teacher("Z.X.W",20,8000)
S=Student("L.C",20,90)

print()

members= [T,S]
for member in members:
    member.tell()
    
    
         
