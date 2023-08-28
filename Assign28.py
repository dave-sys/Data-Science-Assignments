#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 15:47:51 2018

@author: student
"""
#David Dorado
#Date: April 9th
#The confidence interval is 74.3 to 140.8 and the mean is 107.6


import pandas as pd 
import scipy.stats as st

idbm= pd.read_csv('imdb_1000.csv')

comedy= idbm['genre'] == 'Comedy'
comedy_movies= idbm[comedy]
comedy_duration= comedy_movies['duration']

average= comedy_duration.mean()

sigma= comedy_duration.std()

duration_data= len(comedy_duration) 

ci = st.t.interval(0.90,duration_data - 1,loc = average, scale = sigma)

print('The average duration for a comedy film is', average) 
print("Confidence interval:", ci)