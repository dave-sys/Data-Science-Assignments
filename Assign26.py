#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 12:51:27 2018

@author: student
"""

import pandas as pd
import matplotlib.pyplot as plt

movies=pd.read_csv('imdb_1000.csv')

r_rated= movies['content_rating'] == 'R'
R_movies= movies[r_rated]
R_movies_duration= R_movies['duration']

R_movies_duration.plot.box(title= 'R Movies Duration')
plt.show()

g_rated= movies['content_rating'] == 'G'
pg_rated= movies['content_rating'] == 'PG'  
g_and_pg_movies= movies[g_rated | pg_rated]
g_and_pg_duration= g_and_pg_movies['duration']

g_and_pg_duration.plot.box(title= 'G and PG movie Duration')
