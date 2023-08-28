# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 12:13:39 2018

@author: Visoroy
"""
#David Dorado 
#Date: 3.14.as_integer_ratio
#This is a probability code that will find the probability of having a number between 1 and 3 in a number set of 1-6


import pandas as pd 
import random as r 

num_list= []
for i in range(10000):
    num=r.uniform(1,6)
    num_list.append(num)
    
num_series=pd.Series(num_list)

condition= num_series >= 1
condition2= num_series <= 3

conditions= num_series [condition & condition2]

numbers= len(conditions)
orginal= len(num_series)

num_prob= numbers/orginal

print('The probability is', num_prob)