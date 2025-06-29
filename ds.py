import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/andrealoizidou/downloads/US_Accidents_Dec20_Updated.csv", low_memory=False)

# first few rows of the dataframe
print("=====================")
print("DF HEAD()")
print("=====================")
print(df.head())

# descriptive statistics
print("=====================")
print("DESCRIPTIVE STATISTICS")
print("=====================")
print(df.describe())

# info of the dataframe to understand its structure
print("=====================")
print("INFO")
print("=====================")
print(df.info())

# summary of missing values sorted from the most to the least
print("=====================")
print("SUMMARY OF MISSING VALUES")
print("=====================")
missing_values_summary = df.isna().sum().sort_values(ascending=False)
print(missing_values_summary)
print("=====================================")
print("PERCENTAGE OF MISSING VALUES - PLOT")
print("=====================================")
missing_percentage = df.isna().sum().sort_values(ascending = False)/len(df)
plot1 = missing_percentage[missing_percentage != 0].plot(kind = 'bar')
plt.show()
print(plot1)

#printing the states
print(df.State)

#States by accident
states_by_accident = df.State.value_counts()
print(states_by_accident[:10])

#plot2
states_by_accident[:10].plot(kind='bar')

#unique cities
print(df.City)
print(df.City.unique())

#cities by accident
cities_by_accident = df.City.value_counts()
print(cities_by_accident)

#plot3 - citiess by accident
cities_by_accident[:30].plot(kind='bar')
sns.set_style("darkgrid")
sns.histplot(cities_by_accident, log_scale=True)

#cities with a lot of accidents
high_accident_cities = cities_by_accident[cities_by_accident >= 1000]
print(high_accident_cities)

#plot4
sns.histplot(high_accident_cities, log_scale=True)

#cities with lower accidents
low_accident_cities = cities_by_accident[cities_by_accident < 1000]
print(low_accident_cities)

#plot5
sns.histplot(low_accident_cities, log_scale=True)

#percentage of high accident cities
print(len(high_accident_cities)/len(df.City.unique()))

#start time of accident
print(df.Start_Time)

df.Start_Time = pd.to_datetime(df.Start_Time)
print(df.Start_Time.dt.hour)

#plot6 - distribution of time of accidents
sns.histplotstplot(df.Start_Time.dt.hour, bins=24, kde=False, norm_hist=True)

#day of week from start time
monday_start_time = df.Start_Time[df.Start_Time.dt.dayofweek == 0]

#plot7
sns.histplot(monday_start_time.dt.hour, bins=24, kde=False, norm_hist=True)

sundays_start_time = df.Start_Time[df.Start_Time.dt.dayofweek == 6]
#plot8
sns.histplotistplot(sundays_start_time.dt.hour, bins=24, kde=False, norm_hist=True)

#plot 9 for months
sns.histplotstplot(df.Start_Time.dt.month, bins=12, kde=False, norm_hist=True)
