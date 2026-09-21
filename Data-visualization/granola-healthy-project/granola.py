import pandas as pd
import matplotlib.pyplot as plt

df_public = pd.read_csv("healthy-food-survey-public.csv")
#print(df_public)

#calculating the percentage of people who answerd yes and rounding it off

df_public['public'] = df_public.eval('yes / (yes + no + no_opinion)')

df_public['public'] = df_public.eval('public * 100').round()

#

# ok now we drop the columns we dont need 
df_public = df_public[['food', 'public']]
#print(df_public)


#ok now we do the same data cleaning for the experts

df_experts = pd.read_csv('healthy-food-survey-experts.csv')


df_experts['experts'] = df_experts.eval('yes / (yes + no + no_opinion)')


df_experts['experts'] = df_experts.eval('experts * 100').round()


df_experts = df_experts[['food', 'experts']]
#print(df_experts)

#merging the public and expert datasets together and create a new df

df = df_public.merge(df_experts, on='food', how='left')
#print(df)


# visualising paired data with a scatterplot
# each dot represents a food item 
plt.scatter(
    df['public'], 
    df['experts'],
    alpha=0.5
    )

plt.xlabel('Public (%)')
plt.ylabel('Experts (%)')
plt.title('Is food healthy?')

#adding a line
def add_equality_line():
    x = [0, 100]
    y = [0, 100]
    plt.plot(x,y, 
        linestyle='--', 
        alpha=0.5, 
        color='red')    

#a function for squaring the plot and other grid properties
def square_the_plot():
    plt.xlim(0,100)
    plt.ylim(0,100)
    ax = plt.gca()
    ax.set_aspect(1)
    ax.grid(True)

# adding labels for food that public deems healthy
def add_labels(df, x_col, y_col, label_col):
    for (i, row) in df.iterrows():
        x = row[x_col]
        y = row[y_col]
        offset_spacing = "  "
        label = offset_spacing + row[label_col]
        plt.text(x, y, label, va='center', ha='left')

add_equality_line()
square_the_plot()


# adding a column for public minus experts to show diff in opinions

df['public_minus_experts'] = df.eval('public - experts')
df = df.sort_values(by='public_minus_experts', ascending=False)
highest_disagreement = df.head()
print(highest_disagreement)

plt.scatter(df['public'], df['experts'], alpha=0.5)
add_equality_line()
square_the_plot()
add_labels(highest_disagreement, 'public', 'experts', 'food')
plt.show()



#--------------------------------------------------
#full code
def format_plot():
    plt.xlabel('Public (%)')
    plt.ylabel('Experts (%)')
    plt.title('Is food healthy?')
    
def add_equality_line():
    x = [0, 50, 100]
    y = [0, 50, 100]
    plt.plot(x, y, color='black', alpha=0.5, linestyle='--')

def square_the_plot():
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    ax = plt.gca()
    ax.set_aspect(1)

def add_labels(df, x_col, y_col, label_col):
    for (i, row) in df.iterrows():
        x = row[x_col]
        y = row[y_col]
        offset_spacing = "  "
        label = offset_spacing + row[label_col]
        plt.text(x, y, label, va='center', ha='left')

plt.scatter(df['public'], df['experts'], alpha=0.5)
format_plot()
add_equality_line()
square_the_plot()
add_labels(highest_disagreement, 'public', 'experts', 'food')


