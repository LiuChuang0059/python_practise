# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:06:38 2018

@author: dell
"""



def reverse(text):
    return text[::-1]
'''
We use the slicing feature to reverse the text. 
We've already seen how we can make slices from 
sequences using the seq[a:b] code starting from position 
a to position b. We can also provide a third argument that
 determines the step by which the slicing is done.
 The default step is 1 because of which it returns a continuous 
 part of the text. Giving a negative step, i.e., -1 
 will return the text in reverse.
'''

def is_par(text):
    return text  == reverse(text)

sth=input("some text:")

if is_par(sth):
    print("{} is par".format(sth))
else:
    print("{} is not par ".format(sth))