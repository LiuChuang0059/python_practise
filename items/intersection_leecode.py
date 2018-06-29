#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:13:11 2018

@author: liuchuang

给定两个数组，写一个函数来计算它们的交集。
"""


"""
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = set()
        b = set()
        for i in nums1:
            a.add(i)
        for j in nums2:
            b.add(j)
        c = a&b
        return list(c)
"""    
    
    
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums=[]
        for i in nums1:
            if i in nums2 and i not in nums:
                nums.append(i)
        return nums
    


