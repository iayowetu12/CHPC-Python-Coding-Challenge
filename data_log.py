#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:11:52 2022

@author: sir
"""
import datetime
import pandas as pd
mon=[]
day=[]
time=[]
status=[]
f=open("data.log","r")
for line in f:
    linestrip=line.strip().split()
    mon.append(linestrip[0])
    day.append(linestrip[1])
    time.append(linestrip[2])
    status.append(linestrip[-1])
f.close()

df = pd.DataFrame(list(zip(mon, day,time,status)),
               columns =['Month', 'Day','Time_Stamp','Status'])

#===Solution for Question 1
status_on = df.loc[df['Status']=="ON"]

#==Solution for Question 2
df_ts=status_on.loc[:,"Time_Stamp"]
print('PROCESS Duration: ' + str(len(df_ts)))
err=df.loc[df.Status=='ERR']
print('Error Event: \n ' + str(err))