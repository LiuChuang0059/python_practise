# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 22:36:20 2018

@author: dell
"""
import os 


A=[x+x for x in range(1,20)]

B=[x+x for x in range(1,20) if x%2==0]

C=[m*n for m in range(1,5) for n in range(5,10)]

D=[m+n for m in 'ASDFGHJKL' for n in 'Zl']

E=[d for d in os.listdir('.')]


d={'AS':12,'BS':13,'CS':14}
for k,v in d.items():
    print(k, '='   ,v)



L = ['Hello', 'World', 'IBM', 'Apple']
F=[s.lower() for s in L]


M = ['Hello', 'World', 18, 'Apple', None]
G=[q.lower() for q in M if isinstance(q,str) ]

print(A,B,C,D,E,F,G)
