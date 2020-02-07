# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:07:01 2019

@author: İsaYaşasın
"""

import pandas as pd

#1)
data = pd.read_csv("matchinfo.csv")
#2-6)
data.head()
data.tail()
data.columns
data.info()
data.describe

#7)
data['League'].value_counts(dropna=False)
#8-9)
data1 = data[["League","Year","Season","blueTeamTag","bResult","rResult","redTeamTag","gamelength"]]
sütun_isim = ["Lig","Yıl","Sezon","Mavi_Takım","Mavi_sonuç","kırmızı_sonuç","kırmızı_takım","oyun_süresi"]
data1.columns  = sütun_isim

#10-12)
nalcs = data1["Lig"] == "NALCS"
nalcs = data1[nalcs]

eulcs = data1["Lig"] == "EULCS"
eulcs = data1[eulcs]

lck = data1["Lig"] == "LCK"
lck = data1[lck]

#13)
concat = pd.concat([nalcs, eulcs, lck])
concat.shape

#14-16)
data_mavi = data1[["Mavi_Takım","Mavi_sonuç"]]
data_kırmızı = data1[["kırmızı_sonuç","kırmızı_takım"]]
sonuc = pd.concat([data_mavi,data_kırmızı],axis=1)
sonuc.shape

#17)
data_year = pd.read_csv("matchinfo.csv", index_col = "Year")
#18)
sorted_data = data_year.sort_index(axis=0)
#19)
data_2018 = sorted_data.loc[2018,:]
#20)
sütun_isim2 = ["Lig","Mavi_Takım","Mavi_sonuç","kırmızı_sonuç","kırmızı_takım","oyun_süresi"]
veri_2018 = data_2018[["League","blueTeamTag","bResult","rResult","redTeamTag","gamelength"]]
veri_2018.columns = sütun_isim2
#21)
süre = veri_2018["oyun_süresi"] > 50
oyun_süresi = veri_2018[süre]
#22)
pay = oyun_süresi.shape[0]
payda = veri_2018.shape[0]
print(pay/payda)

#23)
def sn(x):
    return x*60
veri_2018["sn_süre"] = veri_2018["oyun_süresi"].apply(sn)
print(veri_2018.head())










