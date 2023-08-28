# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:06:40 2018

@author: Visoroy
"""
#David Dorado
#Date: April 18
#The The scores did improve but every little. The orginal was .78 and increase to .79


import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

sat= pd.read_csv('2012_SAT_Results.csv')

sat.columns=['DBN','School','Takers','Reading_Avg','Math_Avg','Writing_Avg']

#sat.plot.scatter(x='Math_Avg', y='Writing_Avg')
#plt.show()

lm=smf.ols(formula= 'Math_Avg ~ Writing_Avg', data=sat).fit()
print('Rsquare(Writing ~ Math):', lm.rsquared)
#sns.regplot(x='Math_Avg', y='Writing_Avg', data = sat)
#plt.show()

lm2=smf.ols(formula= 'Math_Avg ~ Reading_Avg + Writing_Avg', data=sat).fit()
print('Rsquare(Math ~ Read + Writing):',lm2.rsquared)
#sns.regplot(x='Math_Avg', y='Writing_Avg  Reading_Avg', data=sat)
