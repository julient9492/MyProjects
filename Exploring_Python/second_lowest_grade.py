# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 19:35:26 2022

@author: Roland
"""
names = []
scores = []
result = []
for i in range(int(input())):
    name = input()
    score = float(input())
    names.append(name)
    scores.append(score)   
secondscore = sorted(set(scores))[1]
for j in range(len(scores)):
    if scores[j] == secondscore:
        result.append(names[j])
result.sort
for k in range(len(result)):
    print(result[k])