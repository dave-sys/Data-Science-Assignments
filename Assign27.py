# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 19:42:41 2018

@author: Visoroy
"""
#David Dorado
#Date:4/9
#The mean is 11.3 and the cenfidence interval is -6.87 to 29.54

import pandas as pd
import scipy.stats as st

taxi= pd.read_csv('2016_Green_Taxi_Trip_Data.csv')

fare=taxi['Fare_amount']

fare_mu= fare.mean()
print(fare_mu)

fare_sigma= fare.std()

fare_data= len(fare)

ci = st.t.interval(0.95,fare_data - 1,loc = fare_mu, scale = fare_sigma)

print('The average taxi fare is', fare_mu)
print("Confidence interval:", ci)