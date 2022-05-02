# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 18:24:51 2022
HackerRank - List Comprehensions
@author: Roland
"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range (z+1) if a+b+c != n])
