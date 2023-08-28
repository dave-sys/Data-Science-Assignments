# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:21:32 2018

@author: Visoroy
"""

import pandas as pd
import seaborn as sns

fields= ['Trip_distance', 'Fare_amount', 'Passenger_count', 'Tip_amount']

taxi= pd.read_csv('2016_Green_Taxi_Trip_Data.csv', usecols=fields)

correlation_matrix= taxi.corr()

sns.heatmap(correlation_matrix)
print(correlation_matrix)

