# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:46:22 2022

@author: Roland
"""
n = input()
l = []
for _ in range(int(n)):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "(" + ",".join(args) + ")"
        eval("l."+cmd)
    else:
        print (l)