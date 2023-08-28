# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 18:06:09 2018

@author: David.Dorado
"""
#David Dorado
#Date: Monday, April 30
# So based off my data we can reject the null hypothesis. The total number of trips that have 2 or more passenger and travels 3 or more miles is 1996 and the total taxi trips...
#is 12910 so if you divide that number we get close to .15

import pandas as pd 
import numpy as np

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

population= [1,0]
weight= [probability, 1-probability]

count_list=[]
for i in range(1000):
    sample= np.random.choice(population, p=weight, size=number_taxi_trips)
    count= sum(sample)
    count_list.append(count)
    
count_series= pd.Series(count_list)
count_series.plot.hist(bins=20)

trips_n_passengers= taxi[taxi_trips & more_passenger]
number_total= len(trips_n_passengers)

print('The number of taxi trips with 2 or more passengers and travels 3 or more miles are', number_total)