# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 23:52:34 2018

@author: dell
"""

class Robot:
    
    population=0
    
    def __init__(self,name):
        self.name= name
        print("Initial {}".format(self.name))
        Robot.population = Robot.population + 1
    
    #robert is dying 
    def die(self):
        print("{} has been destroyed".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one Robert ".format(self.name))
        else:
            print("There is still {:d} robert".format(Robot.population))
            
            
    def say_hi(self):
        print("greetings you can call me {}".format(self.name))
        
    #print the current population
    @classmethod
    #refre to a class variable
    def how_many(cls):
        print("we have {:d} roberts".format(cls.population))
        
        
droid1=Robot("L")
droid1.say_hi()
Robot.how_many()

        
droid2=Robot("C")
droid2.say_hi()
Robot.how_many()

droid1.die()
droid2.die()
Robot.how_many()

    