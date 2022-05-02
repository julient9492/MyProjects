# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 11:23:09 2022

@author: Julien T.

"""

#top section
size = int(input("Size: "))
width = (((size * 2) - 1) * 2 ) - 1
str = []
low = []
for i in range(size):
    str2 = []
    lead_letter = chr(ord('a') + (size - i - 1))
    str.append(lead_letter)
    for j in range(len(str) - 1):
        str2.append(str[(len(str) - 2 - j)])
    str3 = "-".join(str+str2)
    str4 = str3.center(width,'-')
    low.append(str4)
    print(str4)
    
#lower section
for i in range(size-1):
    print(low[size - 2 - i])