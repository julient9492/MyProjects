# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 23:05:40 2022

@author: Roland
"""

import numpy
n,m = input().split()
n = int(n)
a = []
b = []
for i in range(n):
    a.append(input().split()) 
for j in range(n):
    b.append(input().split())
A = numpy.array(a, int)
B = numpy.array(b, int)
print(A+B)
print(A-B)
print(numpy.multiply(A, B))
print(A // B)
print(numpy.mod(A, B))
print(numpy.power(A, B))
