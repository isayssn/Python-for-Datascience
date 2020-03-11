# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

df = pd.read_csv("property data.csv")
print(df)
df = df.drop(["PID"], axis = 1)
print(df)
#
##Standard Missing Values
print(df['ST_NUM'])
print(df['ST_NUM'].isnull())
#
##Non-Standard Missing Values
print(df['NUM_BEDROOMS'])
print(df['NUM_BEDROOMS'].isnull())


missing_values = ["n/a", "na", "--"]
df = pd.read_csv("property data.csv", na_values = missing_values)
#
#print(df['NUM_BEDROOMS'])
#print(df['NUM_BEDROOMS'].isnull())
#
#Unexpected Missing Values
#print(df['OWN_OCCUPIED'])
#print(df['OWN_OCCUPIED'].isnull())
#
#cnt=0
#for row in df['OWN_OCCUPIED']:
#    try:
#        int(row)
#        df.loc[cnt, 'OWN_OCCUPIED']=np.nan
#    except ValueError:
#        pass
#    cnt+=1


#Summarizing Missing Values
#print(df.isnull().sum())
#print(df.isnull().values.any())
#
#print(df.isnull().sum().sum())
#

#Replacing
#df['ST_NUM'].fillna(125, inplace=True)
#df.loc[2,'ST_NUM'] = 125
#median = df['NUM_BEDROOMS'].median()
#df['NUM_BEDROOMS'].fillna(median, inplace=True)



























