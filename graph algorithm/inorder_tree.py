#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 00:20:40 2018

@author: liuchuang


树的遍历 

前序 
中序 
后

"""


def preorder(tree):
    '''
    外部函数编写
    前序遍历
    '''
    if tree:
        print(tree.GetRootVal())
        preorder(tree.GetLeftChild())
        preorder(tree.GetRightChild())


def inorder(tree):
    '''
    中序遍历
    '''
    if tree != None:
        inorder(tree.GetLeftChild())
        print(tree.GetRootVal())
        inorder(tree.GetRightChild())



















