import pandas as pd
import matplotlib.pyplot as plt

survey_df = pd.read_csv('coffee-survey-results.csv')
# print(survey_df)

# displaying the colum names
# print(survey_df.columns)

# from the entire df we are only extracting the
# needed columns by putting them in a list then into a new df
needed_columns = [
    "What kind of dairy? (Whole milk)",
    "What kind of dairy? (Skim milk)",
    "What kind of dairy? (Half and half)",
    "What kind of dairy? (Coffee creamer)",
    "What kind of dairy? (Flavored creamer)",
    "What kind of dairy? (Oat milk)",
    "What kind of dairy? (Almond milk)",
    "What kind of dairy? (Soy milk)"
]

dairy = survey_df[needed_columns]
# print(dairy)

# ok now we rename the columns using dictionary that takes
# in the old value as the key and the new value as
# the new name
name_map = {
    # this is a dictionary(map)
    'What kind of dairy? (Whole milk)': 'Whole milk',
    'What kind of dairy? (Skim milk)': 'Skim milk',
    'What kind of dairy? (Half and half)': 'Half and half',
    'What kind of dairy? (Coffee creamer)': 'Coffee creamer',
    'What kind of dairy? (Flavored creamer)': 'Flavored creamer',
    'What kind of dairy? (Oat milk)': 'Oat milk',
    'What kind of dairy? (Almond milk)': 'Almond milk',
    'What kind of dairy? (Soy milk)': 'Soy milk',
}

# now we rename with the rename function
dairy = dairy.rename(columns=name_map)
# print(dairy)

# using the isna() method to check how many not NaN columns we have
# print(dairy.isna().sum())

# This particular survey had a question that asks if you
# add any dairy to yourcoffee. If the respondent answered
# "No", the dairy part of the
# survey was skipped entirely.

# removing columns that have NaN(no proper data) with the dropna()
dairy = dairy.dropna()
# print(dairy)

# ok so the data is cleaned, now we can query the data for answers
# We us the mean on the columns to get the avarage in decimal
# and X100 to get the % value

dairy_preferences = dairy.mean() * 100
# print(dairy_preferences)
# if u want the mean of a row u should pass axis=1 in the mean method

# ok so now we plot the data with a barh graph
dairy_preferences = dairy_preferences.sort_values() # ascending=False)
# print(dairy_preferences)


#_____________________________
# using a series to plot
plt.barh(
    dairy_preferences.index,
    dairy_preferences
   )
plt.xlabel('Percent')
plt.show()
#_____________________________

# changing the series into a 2D df using .reset_index()
df = dairy_preferences.reset_index()
df.columns = ['Dairy Type','Percentage']

plt.barh(
    df['Dairy Type'],
    df['Percentage']
    )
plt.xlabel('Percent')
plt.show()


