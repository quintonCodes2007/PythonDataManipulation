import pandas as pd


# ----------- Definitions ----------------------
# Series
# -> A Pandas Series is one column of data (or one list of results) with an index attached.
# Pandas
# -> Pandas is a Python library used for data manipulation and analysis, especially for tabular (table-like) data.
# DataFrame
# -> A DataFrame is a 2-dimensional table made of rows and columns.
# Head & Tail
# -> Head shows the first 5 rows and tail shows the last f rows in a table.
# loc & iloc
# -> loc selects data by labels and iloc selects data by index position
# Shape
# -> returns the number of rows and columns in a DataFrame.


#---------------------------------------------------------------
# empty dataframe init
# df = pd.DataFrame()

# adding a column
# df['day'] = ['mon','tue','wed']
# df['month'] = ['jan','feb','mar']

# creating a frame from an obj
# obj = {'ones':[1,2], 'tens':[10,20], 'hundreds':[100,200]}
# person = {'name':['quinton','michael'], 'age':[20,19], 'gender':['male', 'male']}
# df2 = pd.DataFrame(person)

# copying and adding to a dataframe
# df2_copy = pd.DataFrame(df2)
# df2_copy['b_balance'] = [10000, 20000]

# other important parts
# print(df2.index)
# print(df2.columns)
# print(df2.shape)

# column calculations (series)
# df3 = pd.DataFrame()
# df3['shape'] = ['triangle', 'square', 'circle', 'rectangle']
# df3['#_sides'] = [3,4,0,4]
# df3['Area'] = [3.4, 4.2, 2, 5.7]


# print(df3['#_sides'].min())
# print(df3['#_sides'].max())
# print(df3['#_sides'].mode())
# print(df3['#_sides'].mean())
# print(df3['#_sides'].median())
# print(df3['#_sides'].sum())
# print(df3['#_sides'].std())
# print(df3['#_sides'].var())
# print(df3['#_sides'].count())

# rows
# print(df3.iloc[1])
# print(df3.loc[:, 'shape'])
# print(df3.loc[3, 'shape'])
# print(df3.loc[[0,2]])
# print(df3.loc[0:2])

# Loading data from files
#  -> csv files are converted into dataframe objects
# df4 = pd.read_csv('practice.csv')
# print(df4)
# print(type(df4))
# print(df4.head())
# print(df4.tail())
# print(df4['gender'].value_counts())

# -------------------------------------------------------
# -------------- Core Pandas moves ----------------------
# df5 = pd.DataFrame()
# df5 = pd.read_csv('right angle triangles.csv')


#_________EVAL()______________
# -> The eval() method does calculations. It's an efficient way to create new columns from a formula.

# adding a new area column using the eval function
# df5['Area'] = df5.eval('0.5 * length * breadth')
# print(df5)

# more eval function calls,
# u can also create a variable and just add it to a column like id = 10 and df5.eval('length +@like')
# df5['length + 2'] = df5.eval('length + 2')
# df5['squared'] = df5.eval('length*length')
# df5['breadth - length'] = df5.eval('breadth - length')
# print(df5)

#_________QUERY()_____________
# -> The query() method finds rows for a given condition. It's an efficient way to filter a dataframe and get the rows you want.

students_df = pd.read_csv('students.csv')


# print(students_df.query('age > 21'))
# 
# print(students_df.query('course == "Math"'))
# 
# print(students_df.query('age == age.min()'))
# 
# print(students_df.query('attendance in'))

# u can also use 'name > "c"' to only get names from d
# for string match u can also use 'name in ["ana", "cat"]' to see any matches from a list
# for numericals u can use .max() .min() .mean() .std() etc...

#______________GROUPBY()_____________
# -> The groupby() method groups rows that share a common value. Once grouped, we can perform aggregation calculations, such as min(), max(), mean() and sum().
# -> this function is really imortant when you need to find stuff like revenue or different avgs at the same time 
# here we create three groups from the course column and call or view the math group
groups = students_df.groupby('course')
print(groups.get_group('Math'))

# after creating groups we use the .mean() to see the avg attendance or age of each group
print(groups['attendance'].mean())
series = groups['age'].mean()


# viewing the avg attendance of all three courses in one line with reset index making the course as a column
students_df.groupby('course')['attendance'].mean().reset_index()



