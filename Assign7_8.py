#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:13:41 2018

@author: student
"""
#David Dorado
#Date:Feb. 20
#This is a code that shows the passenger count in Taxis in 2016 from Feb.11
#This is code that shows the median and mean from the previous code

import pandas as pd
taxi=pd.read_csv('/Users/student/Downloads/2016_Green_Taxi_Trip_Data (1).csv')
taxi['Passenger_count'].plot.hist(bins=7,title='Feb. 11 Passenger Count 2016')
mean=taxi['Passenger_count'].mean()
print('The mean passenger count is',mean)
median=taxi['Passenger_count'].median()
print('The median passenger count is',median)
import matplotlib.pyplot as plt
plt.axvline(mean,linestyle='dashed',linewidth=4,color='red')
plt.axvline(median,linestyle='dashed',linewidth=4,color='black')