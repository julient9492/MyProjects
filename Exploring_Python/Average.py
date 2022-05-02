# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 22:06:02 2022
Average_of_3_grades
@author: Roland
"""
n = int(input())
student_marks = {}
for i in range(n):
name, *line = input().split()
scores = list(map(float, line))
student_marks[name] = scores
query_name = input()
average = sum(student_marks[query_name]) / 3
print('{:.2f}'.format(average))