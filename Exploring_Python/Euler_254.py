# -*- coding: utf-8 -*-

"""
Created on Tue Apr 12 16:52:11 2022
--- Project Euler #254 ---

After trying to solve by brute force, and failing around n=47, 
this code is an attempt to reconstruct the smallest n by 
making combinations of the previous numbers found, which
are stored in dict1.

This program fails at n=37 because the number we are looking for
is 13339, and it is not a combination of previous numbers...


@author: Julien Tardy

"""
import math

def f(n):
    fsum = 0
    for i in str(n):
        fsum += math.factorial(int(i))
    return fsum

def sf(n):
    sfsum = 0
    for i in str(n):
        sfsum += int(i)
    return sfsum

def g(i):
    ls = []
    if i == 1:
        for n in range(1,10):
            dict1[math.factorial(n)] = n
    if i % 9 == 0:
        min_num_digits = i // 9
    else:
        min_num_digits = i // 9 + 1
    a1, a2, a3, a4, a5, a6 = 1        
    for i in range(min_num_digits, 7):
        
        
                
    
                    
def sg(i):
    gsum = 0
    for k in str(i):
        gsum += int(k)
    return gsum

dict1 = {}
results = []
n = 10**18
bigsum = 0
nums =  (input("Enter n: "))
j = nums[0] 
m = nums[1]
for l in range(1, int(nums) + 1):
    bigsum += sg(g(l))
print(bigsum)
    