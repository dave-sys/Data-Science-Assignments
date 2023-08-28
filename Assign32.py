# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:06:40 2018

@author: Visoroy
"""
#David Dorado
#Date: April 17
#My prediction for a 400 score on the math SAT will lead to a 350 score on the writing SAT
#My prediction for a 450 score on the math SAT will lead to a 400 score on the writing SAT


import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

sat= pd.read_csv('2012_SAT_Results.csv')

sat.columns=['DBN','School','Takers','Reading_Avg','Math_Avg','Writing_Avg']

sat.plot.scatter(x='Math_Avg', y='Writing_Avg')
plt.show()

lm=smf.ols(formula= 'Writing_Avg ~ Math_Avg', data=sat).fit()
sns.regplot(x='Math_Avg', y='Writing_Avg', data = sat)