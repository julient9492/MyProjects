# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 18:59:59 2022
HackerRank Runner-Up! 
@author: Roland
"""

n = int(input())
arr = map(int, input().split())
numbers = sorted(list(set(arr)),reverse=True)
print(numbers[1])