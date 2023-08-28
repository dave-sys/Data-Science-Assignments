#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:31:21 2018

@author: student
"""
#David Dorado
#Date: Monday, April 23
#The null hypothesis should be rejected since the number of people who get the flue varies from approximately 15-5


import pandas as pd
import numpy as np

population= ['Flu', 'No_Flu']
weight= [0.1, 0.9]

number_list= []
for i in range(100):
    sample_array= np.random.choice(population, p= weight, size= 100)
    sample= pd.Series(sample_array)
    counts= sample.value_counts()
    num= counts['Flu']
    number_list.append(num)
    
number_series= pd.Series(number_list)
number_series.plot.hist(bins=20)
