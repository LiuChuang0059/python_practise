#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:33:02 2018

@author: liuchuang


use list to implement tree

.
"""

import pprint


Mytree=['a', ##root
        ['b',  ##  leftchild  left_subtree
         ['d',[],[]],
         ['e',[],[]]],
        ['c', ### 1st rightchild righr sub-tree
         ['f',[],[]]]
        ]
####Mytree[0]: root   Mytree[1] leftsubtree  Mytree[2]: right_subtree      
pprint.pprint(Mytree)
print(Mytree[1])
print(Mytree[2])


def BinaryTree(r):
    ###构造一个具有根结点和两个子列表为空
    return [r,[],[]]


def InsertLeftBranch(root,newBranch):
    ###添加左子树 
    t = root.pop(1)
    if len(t) > 1:
        ##左child有值
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])


def InsertRightBranch(root,newBranch):
    ###添加右子树 
    t = root.pop(2)
    if len(t) > 1:
        ##左child有值
        ###原值一定在newbranch 右边
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])


def GetRootValue(root):
    ### 获取根结点值
    return root[0]


def SetRootValue(root,newVal):
    root[0]=newVal


def GetLeftChild(root):
    ### get the left subtree
    return root[1]

def GetRightChild(root):
    ### get the right subtree
    return root[2]

























