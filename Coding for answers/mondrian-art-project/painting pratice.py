import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Painting practice
features = pd.read_csv('mondrian-painting-features.csv')
painting_info = pd.read_csv('mondrian-painting-info.csv')
# print(features)

b104_features = features.query('painting_id == "b104"')
# print(b104_features)

# ok now we are gonna draw a painting with the info from features df
# using a function




def draw_mondrian( painting_id):
    rects = features.query('painting_id == @painting_id')
    total_width = rects.eval("x + width").max()
    total_height = rects.eval("y + height").max()
    
    fig, ax = plt.subplots()
    
    for (idx, row) in rects.iterrows():
        x, y, w, h, rgb = row[['x','y','width','height','rgb']]
        patch = mpatches.Rectangle((x, y), w, h, facecolor=rgb)
        ax.add_patch(patch)
    
    ax.axis([0, total_width, 0, total_height])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.text(0.5, 0.01, painting_id, ha="center", fontsize=14)
    plt.show()
    
# draw_mondrian("b294")


# grouping the features and then checking how many features each painting has
num_of_features = features.groupby('painting_id').size()
# print(num_of_features)
# the result is series with the painting id as the index 

# now we reset the index and turn the series into a dataframe
show_complexity = num_of_features.reset_index(name='complexity')
# print(show_complexity)


# if we want to plot the complexity over time with the paintings
# we need first merge the two dfs
# so here we joined the show_complexity df with painting_info
painting_info = painting_info.merge(
    show_complexity,
    on='painting_id',
    how='left'
)
# print(painting_info)

# now we plot the complexity over time, using a scatterplot
plt.scatter(
    painting_info['year'],
    painting_info['complexity']
    )
plt.xlabel('Year')
plt.ylabel('Complexity')
    
# plt.show()

# now we check if a painting is fake
fp26_features = pd.read_csv('fp26-features.csv')
print(fp26_features)

# recreating the plot from earlier to add a point
plt.scatter(
    painting_info['year'],
    painting_info['complexity']
    )
plt.scatter(
    x = 1926,
    y = 54,
    color = 'red',
    marker= 's'
    )
plt.xlabel('Year')
plt.ylabel('Complexity')
plt.show()


