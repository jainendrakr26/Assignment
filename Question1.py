# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 22:26:43 2020

@author: Jainendra
"""

start=2000
end=3200

for i in range(start,end):
    if (i%7==0) and (i%5!=0):
        print(i,end=",")
        

