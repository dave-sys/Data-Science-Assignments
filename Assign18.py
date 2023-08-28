#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 17:06:26 2018

@author: student
"""
#David Dorado
#Date:3/13
#So the probabilty of getting a call for hot water or heat problem is .071 or 14.92 
#Perhaps the answer is off becuase of the csv has various descriptor 
#the date was feb. 27 2018

import pandas as pd
request=pd.read_csv('311_Service_Requests_from_2010_to_Present.csv')
complaint=request['Complaint Type']
heat= complaint == ('HEAT/HOT WATER')
#print(heat)
des=request['Descriptor']
entire=des ==  ('ENITRE BUILDING')


joint= request[heat]
size=len(joint)
total=len(entire)
prob=total/size
print(prob)

prob2=size/total
print(prob2)

