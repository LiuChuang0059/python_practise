#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 21:37:56 2018

@author: liuchuang


use node to implement tree


"""
import list_tree

class BinaryTree:
    def __init__(self,rootobj):
        #### 树的根对象 可以是对任何对象的引用
        self.key=rootobj
        self.leftchild=None
        self.rightchild=None
        
    def InsertLeftChild(self,newNode):
        '''
        add left subtree 
        create a new binary object
        use self.leftchild to merge it
        '''
        if self.leftchild == None:
            self.leftchild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            ### add old node into the left of t (next layer)
            t.leftchild = self.leftchild
            ### add t into left of root
            self.leftchild = t
            
            
    def InsertRightChild(self,newNode):
        '''
        add left subtree 
        create a new binary object
        use self.leftchild to merge it
        '''
        if self.rightchild == None:
            self.rightchild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            ### add old node into the left of t (next layer)
            t.rightchild = self.rightchild
            ### add t into left of root
            self.rightchild = t
            
            
    def GetRightChild(self):
        ### get the value of right child
        return self.rightchild
    
    def GetLeftChild(self):
        ###
        return self.leftchild
    
    def SetRootVal(self,obj):
        self.key=obj
        
    def GetRootVal(self):
        return self.key
    
r=BinaryTree('a')   
print(r.GetRootVal())
print(r.GetLeftChild())

r.InsertLeftChild('b')
print(r.GetLeftChild())
print(r.GetLeftChild().GetRootVal())

r.InsertRightChild('c')
print(r.GetRightChild())
print(r.GetRightChild().GetRootVal())
r.GetRightChild().SetRootVal('hello world')
print(r.GetRightChild().GetRootVal())












    
    

