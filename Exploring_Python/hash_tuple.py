# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:01:46 2022
Hash_tuple
@author: Roland
"""
n = int(input())
integer_list = map(int, input().split())
mytuple = tuple(integer_list)
print(hash(mytuple))