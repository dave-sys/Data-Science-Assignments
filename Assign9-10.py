#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:09:00 2018

@author: student
"""
#David Dorado
#Date:2/22
#This is a code that uses five or more numbers to show equal mean and median but different variance 
#Update: This new piece of shows a box and whiskers plot of data 1 and data 2

import pandas as pd
import matplotlib.pyplot as plt

alpha_data=pd.Series([1,2,3,4,5])
beta_data=pd.Series([1,1,2,2,3,3,4,4,5,5])

print('The mean for data 1 is',alpha_data.mean())
print('The mean for data 2 is',beta_data.mean())
print('The median for data 1 is',alpha_data.median())
print('The median for data 2 is',beta_data.median())
print('The variance for data 1 is',alpha_data.var())
print('The variance for data 2 is',beta_data.var())

#print(alpha_data.describe())
#print(beta_data.describe())

alpha_data.plot.box(title="Boxplot of data 1",vert=False)
plt.show()
beta_data.plot.box(title='Boxplot of data 2', vert=False)
plt.show()