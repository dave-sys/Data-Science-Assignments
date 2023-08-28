#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:43:13 2018

@author: student
"""
#David Dorado
#Date: 2/27/18
#Question 1: The number of sample size of at least 10000
#Question 2: It seems that the population won't be symmetric the sample number is to low
#Question 3: The number of sample rows should be around 50000 to have some symmetric shape but it will start looking symmetric earlier as well


import pandas as pd
import matplotlib.pyplot as plt

taxi=pd.read_csv('2016_Green_Taxi_Trip_Data.csv')

mean = taxi['Passenger_count'].mean()
print('The mean is',mean)

count_list=[]
for i in range(100):
    taxi_sample=taxi.sample(5)
    count=taxi_sample['Passenger_count'].mean()
    count_list.append(count)

taxi_count=pd.Series(count_list)
taxi_count.plot.hist(bins=20)
plt.axvline(mean,linestyle='dashed',linewidth=2,color = 'black')

