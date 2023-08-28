#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 15:29:00 2018

@author: student
"""
#David Dorado
#Date: March 26
#Q1. For the most part the mean stays the around the same range but the standard deviation increases by around ~2.
#Q2. Again the mean stays around the same range but the standard deviation decreases this time to around ~.4. This graph more closer to the predicted graph.


import pandas as pd


taxi=pd.read_csv('2016_Green_Taxi_Trip_Data.csv')

fare_amount=taxi['Fare_amount']

mu_mean= fare_amount.mean()
#print(mu_mean)

sigma= fare_amount.std(ddof=0)

n=500

sample_list=[]
for i in range(1000):
    amount_sample= fare_amount.sample(n, replace=True)
    sample_mean= amount_sample.mean()
    sample_list.append(sample_mean)
    
sample_series= pd.Series(sample_list)

sample_series.plot.hist(bins=30)

print('mean of sample is', sample_series.mean())
print('Standard deviation of sample mean is', sample_series.std(ddof=0))
