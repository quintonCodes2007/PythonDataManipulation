# practice data analytics stuff

import pandas as pd

df = pd.read_csv('first-day-of-week.csv')
# print(df.head(10))

# displaying column names and number of rows
# print(df.columns)

# printing the number of rows in a df
# print(df.shape)
# print(df.shape[0])

# finding unique values in a column
# the first shows the possible diff values
# and the second shows the number of unique values
# print(df['first_day'].unique())
# print(df['first_day'].nunique())

# filtering rows
# print(df.query('first_day == "mon"'))

# counting rows with certain values
# metric_df = df.query('units == "metric"')
# print(metric_df)

# ok trying the real way
# print(df['units'].value_counts())

# trying to group data by firstday
# day_groups = df.groupby('first_day').size()
# print(day_groups)

# finding the audacious country
print(df.query('first_day == "fri"')['territory'])








