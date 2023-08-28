#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 17:01:16 2018

@author: student
"""
#David Dorado
#Date: March 27
#Q&A.Based of the boxplot drama films tend to have a longer run time becuase the distrubation of duration is much bigger than the ainmated films.


import pandas as pd
import matplotlib.pyplot as plt


idbm= pd.read_csv('imdb_1000.csv')

animated= idbm['genre'] == 'Animation'
animated_movies=idbm[animated]
animated_duration=animated_movies['duration']

animated_duration.plot.box(title='Run Time of Animated Films')
plt.show()

drama= idbm['genre'] == 'Drama'
drama_movies=idbm[drama]
drama_duration=drama_movies['duration']

drama_duration.plot.box(title='Run Time of Drama Films')

