# -*- coding: utf-8 -*-
"""
Created on Sat May 26 12:21:04 2018

@author: 刘闯

贪婪算法  greedy 

求解全覆盖 所需要最少的点

"""

#需要的数字集合
number_needed=set([3,5,6,7,8])

#字母包含的数字

graph={}
graph['A']=set([1,2,3,4])
graph['B']=set([2,3,5])
graph['C']=set([3,5,6])
graph['D']=set([3,7,8,2])

#需要最少的字母列表
char_selection=[]

#循环 直到 需要的字母集合为空
while number_needed :
    best_char=None
    ##字母包含的数字和需要数字的集合
    number_covered=set()  
    
    for  char, num in graph.items():
        covered=num & number_needed
        if len(covered) > len(number_covered):
            number_covered=covered
            best_char=char
    ##添加 重合最多的字母
    char_selection.append(best_char)
    ###从待需要集合 减去 选出的数字
    number_needed=number_needed-number_covered

print(char_selection)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            