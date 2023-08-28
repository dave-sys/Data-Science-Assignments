#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 16:25:56 2018

@author: student
"""
#David Dorado
#Date: March 26
#Q1. The mean is consistant and the standard deviation idecrease by ~.01. The Histogram looks a little similar 
#Q2. The mean is consistant once again and the standard deviation is close to the predicted standard deviation. As for the histogram it looks similar as before


import pandas as pd
import random as r 


#interval= pd.Series([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])


#interval_mu= interval.mean()

#interval_sigma= interval.std(ddof=0)
 
intervals_list=[]
for i in range(1000):
    intervals=r.uniform(1,20)
   
    intervals_list.append(intervals)
    
int_series= pd.Series(intervals_list)

int_mean= int_series.mean()
int_sigma= int_series.std(ddof=0)


n=500

interval_list=[]
for i in range(1000):
    intervals_list=[]
    for i in range(1000):
        intervals=r.uniform(1,20)
   
        intervals_list.append(intervals)
    
    int_series= pd.Series(intervals_list)

    int_mean= int_series.mean()
    int_sigma= int_series.std(ddof=0)
    interval_list.append(int_mean)

interval_series=pd.Series(interval_list)

interval_series.plot.hist(bins=30)

print('Mean of interval is',interval_series.mean())
print('Standard deviation of sample mean is', interval_series.std(ddof=0))