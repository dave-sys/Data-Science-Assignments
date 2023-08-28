# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#David Dorado
#Date; 2/15/17


import pandas as pd
homeless=pd.read_csv('/Users/Markar/.spyder-py3/DHS_Daily_Report.csv')
#homeless.plot(x='Date of Census',y='Total Children in Shelter',title='Children in shelter')
homeless['FractionChildren'] = homeless['Total Children in Shelter']/homeless['Total Individuals in Shelter']
homeless.plot(x = 'Date of Census', y = 'FractionChildren',title='Children in shelter')
