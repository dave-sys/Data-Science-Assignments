#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:17:16 2018

@author: student
"""
#David Dorado
#Date:3/15/2018
#Both graphs have a similar graph and structure and a similar density.
#However, but they do not have the same intervel mainly because one goes from 5 to 10 and the other as 15 to 20
#It is a little unexpected to see that they show a similar density because they are different numbers and each generate different numbers


import pandas as pd
import random as r
import matplotlib.pyplot as plt 

num_list = []
 
for i in range(10000):
     num= r.randint(5,10)
     num_list.append(num)
 
num_series=pd.Series(num_list)

num_series.plot.density()
plt.show()

number_list = []

for i in range(10000):
    number=r.randint(15,20)
    number_list.append(number)
    
number_series=pd.Series(number_list)

number_series.plot.density()
plt.show()