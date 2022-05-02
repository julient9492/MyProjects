# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 20:03:02 2022

HackerRank Doormat Exercise

@author: Julien
"""

bar = '|'
dot = '.'
n,m = input("Enter Width Length \n").split()
n = int(n)
m = int(m)
for j in range((n-1)//2):
    print((((2*j)+1)*(dot + bar + dot)).center(m,'-'))
print("WELCOME".center(m,'-'))
for i in reversed(range((n-1)//2)):
    print((((2*i)+1)*(dot + bar + dot)).center(m,'-'))
