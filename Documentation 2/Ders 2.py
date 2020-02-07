# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:07:33 2019

@author: İsaYaşasın
"""

#import pandas as pd
#import numpy as np

#tips = pd.read_csv("tips.csv")
#tips.info()
#tips.sex = tips.sex.astype("category")
#tips.smoker = tips.smoker.astype("category")
#tips.info()
#
#tips['total_bill'] = pd.to_numeric(tips["total_bill"], errors="coerce")
#tips['tip'] = pd.to_numeric(tips["tip"],errors="coerce")
#tips.info()
#
#
##Clean data with function
#def recode_gender(gender):
#    if gender == "Female":
#        return 0  
#    elif gender == "Male":
#        return 1 
#    else:
#        return np.nan
#tips['recode'] = tips.sex.apply(recode_gender)


#Rearranging and reshaping data
#users = pd.read_csv("users.csv")
#
#visitors_pivot = users.pivot(index="weekday",columns="city",values="visitors")
##print(visitors_pivot)
#
#pivot = users.pivot(index='weekday', columns='city')
#signups_pivot = users.pivot(index='weekday', columns='city', values='signups')


#groupby komutu ileride anlatılacaktır
#group = users.groupby(["city","weekday"]).sum()
#print(group)
#//////////////////////////////////////////////
#Stacking & unstacking
#byweekday = group.unstack(level="weekday")
##print(byweekday)
#
#weekday = byweekday.stack(level="weekday")
##print(weekday)
#
#bycity = group.unstack(level="city")
#print(bycity)
##
#city = bycity.stack(level="city")
##print(city)
##
#swap = city.swaplevel(0, 1)
##print(swap)
#sort = swap.sort_index()
##print(sort)
###
##print(group)
#print(sort.equals(group))
#////////////////////////////////////////////////
#Melting

#visitor_melt = pd.melt(users,id_vars=['weekday'], value_vars = ["visitors"])
#signup_melt = pd.melt(users,id_vars=['weekday',"city"], value_vars = ["signups"])
##print(visitor_melt)
##print(signup_melt)
#
#visitor_melt_name = pd.melt(users,id_vars=['weekday'], value_vars = ["visitors"], var_name = "Günler", value_name= "Değerler")
##print(visitor_melt_name)
#
#
#users_idx = users.set_index(['city', 'weekday'])
##print(users_idx)
#kv_pairs = pd.melt(users_idx, col_level=0, id_vars=['visitors'], value_vars = ["signups"])
##print(kv_pairs)
#////////////////////////////////////////////////

#pivot table
#by_city_day = users.pivot_table(index='weekday', columns='city')
#print(by_city_day)
#
#count_by_weekday1 = users.pivot_table(index='weekday', aggfunc="count")
#print(count_by_weekday1)
#
#signups_and_visitors_total = users.pivot_table(index='weekday', aggfunc=sum, margins=True)
#print(signups_and_visitors_total)

#////////////////////////////////////////////////
#Grouping
#titanic = pd.read_csv("titanic.csv")
#
#by_class = titanic.groupby("pclass")
#count_by_class = by_class["survived"].count()
##print(count_by_class)
#
#by_mult = titanic.groupby(["embarked","pclass"])
#count_mult = by_mult["survived"].count()
##print(count_mult)

#Computing multiple aggregates of multiple columns
#by_class_sub = by_class[['age','fare']]
#aggregated = by_class_sub.agg(["max","median","min"])
##print(aggregated)
##print(aggregated.loc[:, ('age','max')])
##print(aggregated.loc[:,('age','max'):("fare","median")])

#Aggregating on index levels/fields
#gapminder = pd.read_csv("gapminder.csv",index_col=['Year','region','Country']).sort_index()
#by_year_region = gapminder.groupby(level=["Year","region"])
#def spread(series):
#    return series.max() - series.min()
#
#aggregated = by_year_region.agg({'population':'sum', 'child_mortality':'mean', 'gdp':spread})
#print(aggregated.head())


#Grouping on a function of the index
#sales1 = pd.read_csv("sales2.csv")
#sales = pd.read_csv("sales2.csv",index_col="Date",parse_dates=True)
#by_day = sales.groupby(sales.index.strftime("%a"))["Units"].sum()
#print(by_day)


#Detecting outliers with Z-Scores
#gapminder_data = pd.read_csv("gapminder.csv", index_col = ["Country"])
#gapminder_2010 =  gapminder_data['Year'] == 2010
#gapminder_2010 = gapminder_data[gapminder_2010]
#
#
#gapminder2 = gapminder_2010[["fertility","life","population","child_mortality","gdp","region"]]
#from scipy.stats import zscore
#standardized = gapminder2.groupby("region")['life','fertility'].transform(zscore)
#outliers = (standardized['life'] < -3) | (standardized['fertility'] > 3)
#gm_outliers = gapminder2.loc[outliers]
#print(gm_outliers)


#Filling missing data (imputation) by group
#titanic = pd.read_csv("titanic.csv")

#by_sex_class = titanic.groupby(['sex','pclass'])
#print(titanic.age.head(16))

#def fill(empty):
#    return empty.fillna(empty.median())
#titanic.age = by_sex_class.age.transform(fill)
#print(titanic.age.head(16))


#Grouping and filtering with .apply()
#by_sex = titanic.groupby("sex")

#def c_deck_survival(gr):
#    c_passengers = gr['cabin'].str.startswith('C').fillna(False)
#    return gr.loc[c_passengers, 'survived'].mean()
#c_surv_by_sex = by_sex.apply(c_deck_survival)
##print(c_surv_by_sex)


#Grouping and filtering with .filter()

#sales2 = pd.read_csv('sales2.csv', index_col='Date', parse_dates=True)
#by_company = sales2.groupby("Company")
#by_com_sum = by_company["Units"].sum()
#print(by_com_sum)
#by_com_filt = by_company.filter(lambda g:g['Units'].sum() > 35)
#print(by_com_filt)











