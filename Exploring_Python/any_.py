# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 09:51:59 2022
any_
@author: Roland
"""
s = input()
print(any([char.isalnum() for char in s]))
print(any([char.isalpha() for char in s]))
print(any([char.isdigit() for char in s]))
print(any([char.islower() for char in s]))
print(any([char.isupper() for char in s]))