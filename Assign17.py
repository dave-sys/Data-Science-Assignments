#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:10:15 2018

@author: student
"""
#David Dorado
#3/12/2018
#After many attempts I wasn't able to compute a proabiblity for mouse sightings and the reason for this is...
#when you look at the descriptor you only get values for rat sightings... 
#so if you set a df for mouse sighting you will not get none because it doesnt exist
#the only parameters that exist is rodent, in the complaint type, and rodent sighting, in descriptor
#even when doing request.head() mouse sighting does not appear as value/variable  


import pandas as pd

request=pd.read_csv('311_Service_Requests_from_2010_to_Present.csv')


complain_alpha=request['Complaint Type']
rodent=complain_alpha == ('Rodent')

mouse=request['Descriptor']
mouse_sight= mouse == ('Mouse Sighting')


print(request)

#other attempts 

'''
complain=request['Descriptor']
rodent= complain == ('Mouse Sighting')
rodent2= complain == ('Rat Sigthing')
total= rodent.add(rodent2)
#print(total)
percent=len(request[rodent])/len(request[total])
print(percent)

#mouse_sight= len(rodent)/len(total)
#print(mouse_sight)

#num_mouse=len(rodent)
#whole=len(rodent & rodent2)
#prob=num_mouse/whole
#print(prob)
'''