# data cleaning practice
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('top-song-durations.csv')
# print(df.head(10))

# trying to find the shortest song among the head()
# print(df.head()['duration'].min())

# or we can use this line, with index location
# print(df.iloc[:]['duration'].min())
# or
# so this one prints the entire df for the head and entire set
# print(df.query('duration == duration.min()'))
# print(df.head().query('duration == duration.min()'))

# trying to plot these top hit durations over time
# plt.plot(df['year'], df['duration'])
# plt.show()
# but that plot does not show the proper Y-axis values

# print(df.info())
# df.info() just tells us the df infor like colum dtypes

# so we are gonna split the duration strings
split_duration = df['duration'].str.split(':', expand = True)
# print(split_duration.head())

# converting the strings to integers
split_duration = split_duration.astype('int')
# print(split_duration.head())


# ok so we add the three new columns to our df with names
df[['h','m','s']] = split_duration
# print(df.head())

# creating a new total_seconds column
df['total_seconds'] = df.eval('h*3600 + m*60 + s')
# print(df.head())


# ok now we can plot properly
plt.plot(
    df['year'],
    df['total_seconds']
    )
plt.xlabel('Year')
plt.ylabel('total seconds')
# plt.show()

# finding the longest song using iloc or query
print(df.iloc[:-1]['duration'].max())
print(df.query('total_seconds == total_seconds.max()'))


