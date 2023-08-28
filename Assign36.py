# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#David Dorado
#Date:April, 24
# So from the data it seems that people are more likely to click on the red based on the data. Which is very different from the null hypothesis.

import pandas as pd
import numpy as np 

population= ['red', 'blue']
weight=[0.9,0.1]

number_list=[]
for i in range(100):
    sample_array= np.random.choice(population, p=weight, size=3840)
    sample= pd.Series(sample_array)
    counts= sample.value_counts()
    number= counts['blue']
    number_list.append(number)
    
number_series= pd.Series(number_list)
number_series.plot.hist(bins=20) 
    