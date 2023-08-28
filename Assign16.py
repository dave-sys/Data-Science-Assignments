#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 14:19:16 2018

@author: student
"""
#David Dorado
#Date: March 8, 2018
#This is code is a simulation of a the addition of the results of a 4 sided dice and 8 sided dice
#Q&A- Without the bins restriction the graph becomes more symmetrical and with the bins restriction 12 becomes is the outlier 


import pandas as pd
import random as r

dice_list=[]
for i in range(50000000):
    dice= r.randint(1,4) + r.randint(1,8)
    dice_list.append(dice)
    
dice_series= pd.Series(dice_list)
dice_series.plot.hist()
