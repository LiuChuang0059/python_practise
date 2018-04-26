# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 14:54:30 2018

@author: dell
"""

poem = '''


Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

f=open('poem.text','w')
f.write(poem)
f.close

f=open('poem.text','r')
while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line,end=" ")
    
f.close

