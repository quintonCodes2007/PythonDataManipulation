import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("how-couples-met.csv")
#print(df)

# ploting the df on a line graph
#df.plot()
#plt.show()

#making the decade column the index
df = df.set_index('decade')
#print(df)
#df.plot()
#plt.show()

# making the online dating line stand out more
focus_column = 'online'
focus_color = 'C3'
back_columns = [
    'college',
    'at work',
    'through friends',
    'through family',
    'restaurant',
    'neighbors'
    ]
back_colors = ['C0','C1','C2','C4','C5','C6']

# a function to add labels to columns
def add_end_labels(df, x, column_names, alpha):
    for column_name in column_names:
        y = df[column_name].iloc[-1]
        offset_spacing = "  "
        label = offset_spacing + column_name
        plt.text(x, y, label, va="center", alpha=alpha)


# function to remove spines and ticks and stuff
def clean_axes():
    ax = plt.gca()
    ax.spines[['left', 'top', 'right']].set_visible(False)
    ax.tick_params(axis='y', length=0)
    plt.grid(axis='y', alpha=0.5)

# a function to add lables to axes
def add_axes_labels():
    y_ticks = [0, 10, 20, 30, 40, 50]
    y_tick_labels = ['0', '10', '20', '30', '40', '50%']
    plt.yticks(y_ticks, y_tick_labels)
    plt.xlabel('Decade')

df.plot(y=back_columns, color=back_colors, alpha=0.5)
plt.plot(df.index, df[focus_column], color= focus_color, linewidth=5)

# the legend is the key of the graph and we are removing it to set inline lables
plt.legend().set_visible(False)
add_end_labels(df, 2010, back_columns, alpha = 0.5)
add_end_labels(df, 2010, [focus_column], alpha = 1)
clean_axes()
add_axes_labels()
plt.show()


































