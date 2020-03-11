# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 14:39:04 2019

@author: ISA YASASİN
"""

import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [9, 7]

nobel = pd.read_csv("nobel.csv")

#1) So, who gets the Nobel Prize?
nos =  nobel["sex"].value_counts()
non = nobel['birth_country'].value_counts().head(10)


#2) USA dominance
nobel['usa_born_winner'] = nobel["birth_country"]== "United States of America"
nobel['decade'] = (np.floor(nobel["year"] / 10) * 10).astype(int)
prop_usa_winners = nobel.groupby("decade", as_index=False)["usa_born_winner"].mean()
print(prop_usa_winners)

##3) USA dominance, visualized
#plt.plot(prop_usa_winners["decade"], prop_usa_winners["usa_born_winner"])
#plt.show()
#4) What is the gender of a typical Nobel Prize winner?
#nobel['female_winner'] = nobel["sex"] == "Female"
#prop_female_winners = nobel.groupby(["decade", "category"], as_index=False)["female_winner"].mean()

#ax = sns.lineplot(x="decade", y="female_winner", hue="category", data=prop_female_winners)
#plt.show()
#5) The first woman to win the Nobel Prize
first = nobel[nobel["sex"] == "Female"].nsmallest(1,"year")

#6) Repeat laureates
def a(group):
    return len(group) >= 2
more = nobel.groupby("full_name").filter(a)

#7) How old are you when you get the prize?
nobel['birth_date'] = pd.to_datetime(nobel["birth_date"])
nobel['age'] = nobel["year"] - nobel["birth_date"].dt.year

#plt.scatter(nobel["year"],nobel["age"])
#plt.show()
#
#sns.lmplot(x="year", y="age", data=nobel, lowess=True, aspect=2, line_kws={"color" : "black"})
#plt.show()
#
##8) Age differences between prize categories
#sns.lmplot(x="year", y="age", data=nobel, row="category", lowess=True, aspect=2, line_kws={"color" : "black"})
#plt.show()

#9) Oldest and youngest winners¶ 
oldest = (nobel.nlargest(1, "age"))
youngest = (nobel.nsmallest(1, "age"))







