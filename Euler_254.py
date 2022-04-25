# -*- coding: utf-8 -*-

"""
Created on Tue Apr 12 16:52:11 2022
--- Project Euler #254 ---

After trying to solve by brute force, and failing around n=47, 
this code is an attempt to reconstruct the smallest n by 
making combinations of the previous numbers found, which
are stored in dict1.

This program fails at i=37 because the number we are looking for
is 13339, and it is not a combination of previous numbers...
My understanding is that 37 needs to be constructed by taking
9! = 362,880 ==> digitsum = 27 
and adding 19 to it so that we get 362,899 ==> digitsum = 37.
That 19 is obtained by putting together 1333, since
1! + 3! + 3! + 3! = 19.

The solution seems to reside in dealing with all the possible combinations
of k digits that sum up to the desired number...

Example for i = 10:

1:    1! = 1       6:   6! = 720
2:    2! = 2       7:   7! = 5040
3:    3! = 6       8:   8! = 40320
4:    4! = 24      9!   9! = 362880
5:    5! = 120
    
    10 can only be obtained by summing AT LEAST 2 digits
    
    2 digits                        3 digits                            4 digits                                   
    1+9 --> 19 --> 1333             1+0+9 --> 109 --> 1334444           1+0+0+9 --> 1009 --> 144556                ... 
    2+8 --> 28 --> 224              1+1+8 --> 118 --> 223334444             .       .       .                      ...
    3+7 --> 37 --> 1334             1+2+7 --> 127 --> 135                   .       .       .                      ...
    .       .       .               .           .       .                   .       .       .
    .       .       .               .           .       .               5+0+4+1 --> 5041 --> 17
    .       .       .               .           .       .
    9+1 --> 91 --> 1333444          7+2+1 --> 721 -->  16
    
    Here we see that 16 is the smallest number we can reconstruct for i=10.
    

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
    
