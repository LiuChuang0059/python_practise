# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:43:53 2018

@author: 刘闯

快速排序

"""
def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[0]
    # sub-array of all the elements less than the pivot
    less = [i for i in array[1:] if i <= pivot]
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
list=[1,2,3,4,5,6,7,8,9,0,9,8,7,76666,5,4,3,3,2,2222222222,3334,4,5,5,4,3,4,2,3,4,5,6,34,565,34,3,454,6,6,5,7,5,7,6564,4]
print(quicksort(list))
list.sort()
print(list)