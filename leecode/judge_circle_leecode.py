#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 21:50:18 2018

@author: liuchuang
"""

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        u = moves.count('U')
        d = moves.count('D')
        l = moves.count("L")
        r = moves.count('R')
        if u == d and l == r:
            return True
        else:
            return False