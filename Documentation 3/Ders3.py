
import pandas as pd

#Filling missing data (imputation) by groupby
titanic = pd.read_csv("titanic.csv")

by_sex_class = titanic.groupby(['sex','pclass'])
print(titanic.age.head(16))

def fill(empty):
    return empty.fillna(empty.median())
titanic.age = by_sex_class.age.transform(fill)
print(titanic.age.head(16))


#Grouping and filtering with .apply()
by_sex = titanic.groupby("sex")

def c_deck_survival(gr):
    c_passengers = gr['cabin'].str.startswith('C').fillna(False)
    return gr.loc[c_passengers, 'survived'].mean()
c_surv_by_sex = by_sex.apply(c_deck_survival)
print(c_surv_by_sex)


##Grouping and filtering with .filter()
#sales2 = pd.read_csv('sales2.csv', index_col='Date', parse_dates=True)
#by_company = sales2.groupby("Company")
#by_com_sum = by_company["Units"].sum()
#print(by_com_sum)
#
#def func(g):
#    units_35 = g['Units'].sum()
#    return units_35 > 35
#
#by_com_filt = by_company.filter(func)
#print(by_com_filt)
#
#
#
#medals = pd.read_csv("medalists.csv")
#
##Using .value_counts() for ranking
#country_names = medals["NOC"]
#medal_counts = country_names.value_counts()
#print(medal_counts.head(15))
#
##Using .pivot_table() to count medals by typea
#counted = medals.pivot_table(index="NOC",values="Athlete",columns="Medal",aggfunc="count")
#counted['totals'] = counted.sum(axis="columns")
#counted = counted.sort_values("totals", ascending=False)
#print(counted.head(15))
#
##Applying .drop_duplicates()
#ev_gen = medals[["Event_gender","Gender"]]
#ev_gen_uniques = ev_gen.drop_duplicates()
#print(ev_gen_uniques)
#
##Finding possible errors with .groupby()
#medals_by_gender = medals.groupby(["Event_gender","Gender"])
#medal_count_by_gender = medals_by_gender.count()
#print(medal_count_by_gender)
#
##Locating suspicious data
#sus = (medals.Event_gender == 'W') & (medals.Gender == 'Men')
#suspect = medals[sus] 
#print(suspect)
#
##Using .nunique() to rank by distinct sports
#country_grouped = medals.groupby("NOC")
#Nsports = country_grouped["Sport"].nunique()
#Nsports = Nsports.sort_values(ascending=False)
#print(Nsports.head(15))
#
##Counting USA vs. USSR Cold War Olympic Sports
#during_cold_war = (medals.Edition>=1952) & (medals.Edition<=1988)
#is_usa_urs = medals.NOC.isin(['USA', 'URS'])
#cold_war_medals = medals.loc[during_cold_war & is_usa_urs]
#country_grouped = cold_war_medals.groupby('NOC')
#Nsports = country_grouped['Sport'].nunique().sort_values(ascending=False)
#print(Nsports)
#
##Counting USA vs. USSR Cold War Olympic Medals
#medals_won_by_country = medals.pivot_table(index="Edition",columns="NOC",values="Athlete",aggfunc="count")
#cold_war_usa_urs_medals = medals_won_by_country.loc[1952:1988, ['USA','URS']]
#most_medals = cold_war_usa_urs_medals.idxmax(axis="columns")
#print(most_medals.value_counts())








