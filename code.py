# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here

# Data Loading 
data = pd.read_csv(path)
data.head(10)
#Rename 'Total' column
data.rename(columns={'Total':'Total_Medals'},inplace=True)
# Summer or Winter
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter') 
data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])
better_event = data.loc[data['Better_Event'].value_counts().max(),'Better_Event']


# Top 10
def top_ten(df,col_name):
    country_list=[]
    largest = df.nlargest(10, col_name)
    country_list = largest['Country_Name']
    return country_list

top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries.drop(top_countries.index[-1],inplace=True)

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')

summer = set(top_10_summer)
winter = set(top_10_winter)
tot = set(top_10)

com = summer.intersection(winter)
com1 = com.intersection(tot)
common = list(com1)


# Plotting top 10
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

plt.figure(figsize=(14,3))
plt.bar(summer_df['Country_Name'],summer_df['Total_Summer']);

plt.figure(figsize=(14,3))
plt.bar(winter_df['Country_Name'],winter_df['Total_Winter']);

plt.figure(figsize=(14,3))
plt.bar(top_df['Country_Name'],top_df['Total_Medals']);

# Top Performing Countries
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']

summer_max_ratio = [summer_df['Golden_Ratio'].max()]
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

winter_max_ratio = [winter_df['Golden_Ratio'].max()]
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_max_ratio = np.round(top_df['Golden_Ratio'].max(),2)
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']



# Best in the world 
data_1 = data[:-1]

data_1['Total_Points'] = (data_1['Gold_Total']*3)+(data_1['Silver_Total']*2)+(data_1['Bronze_Total']*1)

most_points=data_1['Total_Points'].max()

best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']

# Plotting the best
best = data[data['Country_Name']==best_country]

best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar(figsize=(10,5),stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


