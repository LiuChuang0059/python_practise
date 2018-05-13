# -*- coding: utf-8 -*-
"""
Created on Sun May 13 16:26:54 2018

@author: dell
"""

cities={
        'Dalian':{
                'Location':'A+',
                'Environment':'A+',
                'consume':'B+'
                },
        'Hangzhou':{
                'Location':'A',
                'Environment':'A+',
                'consume':'A+'
                },
        'Shenzhen':{
                'Location':'A',
                'Environment':'A',
                'consume':'A+'
                },
        }
cities['Dalian']['Location']='A-' ###??? 修改字典中的key
cities['DaLian']=cities.pop('Dalian')
for city,infor in cities.items():
    print('\n'+city +'  :')
    for facter,rank in infor.items():
        print('\t'+facter +':  '+ rank)

