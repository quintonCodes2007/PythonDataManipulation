# ocean's deepest divers
import pandas as pd
import matplotlib.pyplot as plt

divers = pd.read_csv('deepest-diving-animals.csv')
# print(divers)

# finding lowest diver in three ways
divers.query('depth == @divers["depth"].max()')

divers[divers['depth'] == divers['depth'].max()]

divers.loc[divers['depth'].idxmax()]

# print(divers)


# checking the diff categories
categories = divers['category'].value_counts()
# print(categories)

# finding the deepest diver in each cat
max_depth = divers.groupby('category')['depth'].max()
# print(max_depths)

# turning the series into a df with reset.index
max_depth = max_depth.reset_index(name='max_depth')
# print(max_depths)


# ------------------------------------------
# a function to hide spines and add faded lines
def clean_bar_axes():
    ax = plt.gca() # get current axis
    ax.spines[['top','bottom','left','right']].set_visible(False)
    ax.grid(axis='x', color='black', alpha=0.5)
    ax.tick_params(axis='both', length=0)
# -----------------------------------------


# ploting with the max categories
max_depth['color'] = 'C0'
max_depth.loc['ref_0'] = ['submarine implosion', 730, 'C3']
max_depth = max_depth.sort_values('max_depth')
plt.barh(max_depth['category'], max_depth['max_depth'], color = max_depth['color'])
plt.xlabel('Maximum depth (meters)')
clean_bar_axes()
plt.show()























