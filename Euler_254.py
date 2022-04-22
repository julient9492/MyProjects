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
    dict2 = dict1.copy()
    ls = []
    if i == 1:
        for n in range(1,10):
            if sf(f(n)) not in dict1:
                dict1[sf(f(n))] = [n]  
            else: 
                dict1[sf(f(n))].append(n)
    if i in dict1:
        ls.append(dict1[i][0])
    for t in dict1:
        u = i - t
        if u < 1:
            continue
        for t1 in dict1[t]:
            for u1 in dict1[u]:
                temp = sorted(list(str(u1) + str(t1)))
                num = "".join(temp)
                sum = sf(f(int(num)))
                if sum not in dict2:
                    dict2[sum] = []
                    dict2[sum].append(int(num))
                else:
                    dict2[sum].sort()
                    if int(num) < dict2[sum][0]:
                        dict2[sum].append(int(num))
                if sum == i:
                    ls.append(int(num))
                    ls.sort()                 
    results.append(ls[0])
    dict1.update(dict2)
    return ls[0]
                    
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
    