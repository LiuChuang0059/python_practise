# -*- coding: utf-8 -*-
"""
Created on Sun May 13 16:09:23 2018

@author: dell
"""
information={
        'Name':'Liu Chuang',
        'Age':20,
        'School':['Haiwan','37th','Wuhan University'],
        'ideal':['Zhejiang','Peking'],
        }
print('Name: '+ information['Name']+ '\n')
print('Age:  '+ str(information['Age'])+ '\n')
print('\nSchool:')
for school in information['School']:
    print(school)
print('\nIdeal:')
for ideal in information['ideal']:
    print(ideal)

