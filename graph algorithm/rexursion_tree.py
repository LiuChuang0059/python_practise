#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 00:13:58 2018

@author: liuchuang


递归 实现 分型树


"""
import turtle


def tree(branchlen,t):
    if branchlen > 5 :
        t.forward(branchlen)
        t.right(20)
        tree(branchlen-15,t)
        t.left(40)
        tree(branchlen-15,t)
        t.right(20)
        t.backward(branchlen)
        

def main():
    t = turtle.Turtle()
    mywin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    mywin.exitonclick()
    
main()