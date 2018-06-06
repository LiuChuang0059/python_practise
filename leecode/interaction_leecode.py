#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:25:06 2018

@author: liuchuang
"""

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
#        if not nums1 or not nums2 or nums1[-1] < nums2[0] or nums1[0] > nums2[-1]
#             return []
        
#         res = []
        
#         i = 0
#         j = 0
        
#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] == nums2[j]:
#                 res.append(nums1[i])
#                 i += 1
#                 j += 1
#             elif nums1[i] < nums2[j]:
#                 i += 1
#             else:
#                 j += 1
#         return res

#        res = []
#        dict1 = {}
#        for i in nums1:
#            if i in dict1:
#                dict1[i] += 1
#            else:
#                dict1[i] = 1
        
#        for i in nums2:
#            if i in dict1:
#                res.append(i)
#                dict1[i] -= 1
#                if dict1[i] == 0:
#                    dict1.pop(i)
#        return res
    
        hash_set = {}
        result = []
        for n in nums1:
            if n not in hash_set:
                hash_set[n] = 1
            else:
                hash_set[n] += 1
        for m in nums2:
            if m in hash_set and hash_set[m] > 0:
                result.append(m)
                hash_set[m] -= 1
        return result
            