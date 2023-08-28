# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 18:06:09 2018

@author: David.Dorado
"""

import pandas as pd 

taxi= pd.read_csv('2016_Green_Taxi_Trip_Data.csv')

passenger= taxi['Passenger_count']
more_passenger= taxi['Passenger_count'] >= 2

number_passenger= len(passenger)
number_more_passenger= len(taxi[more_passenger])

probability= number_more_passenger / number_passenger 

print('Estimated number of passengers in a taxi that is more than 2 is', probability)

