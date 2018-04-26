# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 22:16:28 2018

@author: dell
"""

def findmaxandmin(L):
    if L==[]:
        return(None,None)
    else:
        min=L[0]
        max=L[0]
        for i in L:
            if i<min:
                min=i
            if i>max:
                max=i
        return(min,max)

print(findmaxandmin([]))
