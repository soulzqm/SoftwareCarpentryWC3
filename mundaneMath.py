# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 03:14:50 2019

@author: qimin
"""
"""
start from 0 with step size of 2, and end at 100, add the number 0,2,4,....100 together by "sum"
"""
tol = sum(x for x in range(0,101,2))
print(tol)
