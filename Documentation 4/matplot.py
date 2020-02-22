# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:05:37 2019

@author: şerifekahraman
"""

import matplotlib.pyplot as plt
import pandas as pd

weather = pd.read_csv("weather.csv",index_col= "Date", parse_dates=True)
weather.info()

mean = weather.groupby(weather.index.strftime("%m"))["Mean TemperatureF"].mean()
month = weather.index.strftime("%m")
month_df = pd.DataFrame(month)
month_dup = month_df.drop_duplicates()

##Line Plot 
#plt.plot(month_dup,mean)
#plt.title("Aylık Ortalama Sıcaklık Değerleri (F)")
#plt.xlabel("Aylar")
#plt.ylabel("Sıcaklık(F)")
aylar = ["Ocak","Subat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
#plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12],aylar, rotation = 70)
#plt.show()
#
##Scatter plot
#plt.scatter(month_dup, mean)
#plt.xlabel("Aylar")
#plt.ylabel("Sıcaklık(F)")
#plt.show()
#
##Histogram
#plt.hist(mean, bins=4)
#plt.xlabel("Sıcaklık(F)")
#plt.ylabel("Sıklık")
#plt.show()
#
##Box plot
#plt.boxplot(mean)
#plt.yticks(range(28, 77, 3))
#plt.ylabel("Sıcaklık (F)")
#plt.show()
#
#print(mean.mean())
#print(mean.min())
#print(mean.max())

#Bar chart
number = range(len(month_dup))
plt.bar(number, mean)
plt.xticks(number, aylar, rotation = 70)
plt.yticks(range(0 , 75, 5))
plt.title("Aylık Ortalama Sıcaklık Değerleri (F)")
plt.xlabel("Aylar")
plt.ylabel("Sıcaklık (F)")
plt.show()

##Pie chart
#plt.pie(mean, labels = aylar, autopct = "%.2f")
#plt.show()

















