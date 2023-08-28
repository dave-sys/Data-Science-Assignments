#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:38:35 2018

@author: student
"""
#David Dorado
#Date:2/20
#A plot showing the fraction of DR citizens in the island Hispaniola 
import pandas as pd
islandpop=pd.read_csv('/Users/student/Downloads/islandsHistPop.csv',skiprows=3)
islandpop['Hispaniola']=islandpop['Haiti']+islandpop['Dominican Republic']
islandpop.plot(x='Year',y='Hispaniola')
islandpop['DR']=islandpop['Dominican Republic']/islandpop['Hispaniola']
islandpop.plot(x='Year',y='DR',title='Fraction of DR in Hispaniola')