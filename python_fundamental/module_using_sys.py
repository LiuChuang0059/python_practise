# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 00:06:28 2018

@author: dell
"""

import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')
