import matplotlib.pyplot as plt
import pandas as pd

internet = pd.read_csv('world-internet-users.csv')
population = pd.read_csv('historical-world-population.csv')
# print(internet)
# print(population)
int_user_10M = internet.query('internet_users > 100e6')
# print(int_user_10M.head(1))

# merging the two dataframes together using left merge
# the df that the merge is called on is the main df and keeps all its columns
# left merge finds the columns that are the same in both dfs e.g if the year 2018 is in both df it willl show its row
# inner merge does not show rows that have missing values but left merge shows
# right merge is similer to left but the right df is the main

df = internet.merge(population, on='year', how='left')

# the dropna() function removes any NaN values from any coulum in the resulting df so u can sometimes specify with
# df.dropna(subset=['population']) to only remove NaN values in population
# using left merge and dropna is more safer then inner merge cause with left merge u get more control.
# df = df.dropna()
# print(df.head())

# calculating the percentage of the world that is connected each year
df['percent'] = df.eval('internet_users/population*100')
df['percent'] = df['percent'].round(2)
# print(df)

# plotting the percent connected over time and adding a line at 50% to see when the population exceeded 50%
# plt.plot(df['year'], df['percent'])
# plt.axhline(50, color='red', linestyle='--')
# plt.xlabel('year')
# plt.title('Number of people connected each year')
# plt.ylabel('percent Connected')
# plt.show()

# finding the first year that surpassed 50% of the world population
over_half_connected = df.query('percent >= 50')
over_half_connected.head()
print(over_half_connected)

