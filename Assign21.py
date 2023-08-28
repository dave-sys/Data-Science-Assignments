#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:20:44 2018

@author: student
"""
#David Dorado
#Date:March 20
#My estimate is accurate to the theoretical probability. The estimate is in the .95 to .96 range. 


import pandas as pd
import random as r

number= r.gauss(5,2)
print('Normal distribution:',number)

number_list = []

for i in range(1000):
    num= r.gauss(5,2)
    number_list.append(num)
    
number_series=pd.Series(number_list)

condition_o= number_series <= 9
condition_t= number_series >= 1

sigma= number_series[condition_o & condition_t]

probability= len(sigma)/len(number_series)
print('The estimated probability number with sigma of mean:',probability)
