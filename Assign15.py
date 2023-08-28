# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 19:14:04 2018

@author: Visoroy
"""

#David Dorado
#Date: March 7th, 2018
#This code is a simulation of rolling and adding 3 dice
#Q&A- If you increase the the number of simlations then the probability of rolling 10 and 13 increase a lot more than the other numbers.
#HOwever, if you add bins that range from 4-18 the graph  is symmetrical as shown if you run the coode

import pandas as pd
import random as r
import matplotlib.pyplot as plt

roll_list=[]
for i in range(500000):
    num=r.randint(1,6) + r.randint(1,6) + r.randint(1,6)
    roll_list.append(num)
    
rolls=pd.Series(roll_list)
rolls.plot.hist()
plt.show()
rolls.plot.hist(bins= range(4,18))