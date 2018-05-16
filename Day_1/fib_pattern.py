#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 14:57:26 2018

@author: kullu
"""
a = 0
b = 1
print(a)
print(b,end=" ")
c=a+b
print(c)
for i in range(3,5):
    for j in range(0,i):
        a = b
        b = c
        c = a + b
        print(c,end=" ")
        
    print()