#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:22:03 2018

@author: student
"""
#David Dorado 
#Date:March 20

import pandas as pd
import random

num_list = []
for i in range(100000):
    num= random.gammavariate(2,2)
    num_list.append(num)

series= pd.Series(num_list)

series.plot.hist(bins=200)
