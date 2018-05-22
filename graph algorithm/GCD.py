# -*- coding: utf-8 -*-
"""
Created on Fri May 18 10:25:58 2018

@author: 刘闯

欧几里得算法 求解公约数
"""

#A=Q*B+R  if A>B
def GCD(A,B):
    if A==0:
        gcd=B
    elif B==0:
        gcd=A
    else:
        return GCD(B,A%B)
    return gcd
print(GCD(27,123))
    