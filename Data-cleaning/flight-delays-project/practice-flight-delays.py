# flight delays
import pandas as pd
import matplotlib.pyplot as plt

flights = pd.read_csv('flights.csv')
# print(flights)

# making a df from the scheduled and actual flights
departures = flights[['scheduled', 'actual']]
# print(departures)

# departures.info()

# converting sring values to date time
departures['scheduled'] = pd.to_datetime(departures['scheduled'])
departures['actual'] = pd.to_datetime(departures['actual'])

# print(departures.info())

# this modifies the real flights df instead of the departures view we created
# flights.loc[:, 'scheduled'] = pd.to_datetime(flights['scheduled'])
# flights.loc[:, 'actual'] = pd.to_datetime(flights['actual'])

# calcualting the delays
# departures['delay'] = departures.eval('actual - scheduled')
departures['delay'] = departures['actual'] - departures['scheduled']
print(departures)

# checking which flights are late with using dt.total_seconds()
# Create a boolean column that marks flights as late (True if delay > 15 minutes / 900 seconds)

departures['is_late'] = departures['delay'].dt.total_seconds() > 900
# print(departures)

# getting the day of the week
departures['day_name'] = departures['actual'].dt.strftime('%a')
print(departures)

# grouping the df by day of the week and calculating the mean
# of is_late for each day and converting to percentage
proportion_delayed = departures.groupby('day_name')['is_late'].mean()
percent_delayed = proportion_delayed * 100
# print(percent_delayed)

# changing the index
new_index_order = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
percent_delayed = percent_delayed.reindex(new_index_order)
# print(percent_delayed)

plt.bar(percent_delayed.index, percent_delayed)
plt.ylabel('Percent Delayed')
plt.show()

