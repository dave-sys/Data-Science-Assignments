# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 18:06:09 2018

@author: David.Dorado
"""
#David Dorado
#Date: Monday, April 30


import pandas as pd 
#import numpy as np

taxi= pd.read_csv('2016_Green_Taxi_Trip_Data.csv')

passenger= taxi['Passenger_count']
more_passenger= taxi['Passenger_count'] >= 2

number_passenger= len(passenger)
number_more_passenger= len(taxi[more_passenger])

probability= number_more_passenger / number_passenger 

print('Estimated number of passengers in a taxi that is more than 2 is', probability)

taxi_trips= taxi['Trip_distance'] >= 3
number_taxi_trips= len(taxi[taxi_trips])

print('The number of trips that are 3 or more miles is', number_taxi_trips)

'''
population= [1,0]
weight= [probability, 1-probability]

count_list=[]
for i in range(1000):
    sample= np.random.choice(population, p=weight, size=number_taxi_trips)
    count= sum(sample)
    count_list.append(count)
    
count_series= pd.Series(count_list)
count_series.plot.hist(bins=20)
'''