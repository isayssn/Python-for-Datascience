# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:40:20 2019

@author: ISA YASASİN
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Dropping Columns in a DataFrame
df = pd.read_csv('BL-Flickr-Images-Book.csv')
df.head()

to_drop = ['Edition Statement','Corporate Author','Corporate Contributors','Former owner','Engraver','Contributors','Issuance type','Shelfmarks']
df.drop(to_drop, inplace = True, axis = 1)
#df.drop(columns=to_drop, inplace=True)
df.head()

#Changing the Index of a DataFrame
df['Identifier'].is_unique  
df = df.set_index("Identifier")
df.loc[206]
df.iloc[0]

#Tidying up Fields in the Data
df.info()
df.dtypes.value_counts()

df.loc[1905:, 'Date of Publication'].head(10)

extr = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
extr.head()

df['Date of Publication'] = pd.to_numeric(extr)
df.info()

df['Date of Publication'].isnull().sum()

#Combining str Methods with NumPy to Clean Columns
df['Place of Publication'].head(10)

print("/////////////")
print(df.loc[4157862])
print("/////////////")
print(df.loc[4159587])
print("/////////////")

pub = df['Place of Publication']
london = pub.str.contains('London')
oxford = pub.str.contains('Oxford')

df['Place of Publication'] = np.where(london, 'London',
                                      np.where(oxford, 'Oxford',
                                               pub.str.replace('-', ' ')))

print("/////////////")
print(df.loc[4157862])
print("/////////////")
print(df.loc[4159587])
print("/////////////")

#Analyzing Number of Publisher in London
paris = df[df['Place of Publication'] == "London"]
group = paris.groupby("Date of Publication")["Publisher"].count()
group = group.reset_index()

#Visualizing the outputs
date = group["Date of Publication"]
publisher = group["Publisher"]
plt.plot(date, publisher)
plt.show()

group1 = group.drop([242], axis=0)
date1 = group1["Date of Publication"]
publisher1 = group1["Publisher"]
plt.plot(date1, publisher1)
plt.show()



















