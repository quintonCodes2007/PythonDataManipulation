import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('human_skeleton.csv')


# groups = df.groupby('region')
# this are the two ways to display the number of bones in each region
# by creating groups and the second one is simple
# print(groups['region'].value_counts())
# print()
# print(df['region'].value_counts())

# checking the proportions
# print(df.shape)
# proportion of 
# print(64 + 52 / 204)

# print(df)
# print(df.sort_values(by='fused_from', ascending=False ))

# this is the number of bones babies have
# print(df['fused_from'].sum())

# checking how mayn bones are in the head
# print(df.query('subregion == "neck"'))
# print(df.query('subregion == "neck"'))

# checking which region has the most bones and plotting
bone_count = df['region'].value_counts()
bone_count.plot.bar()
plt.ylabel('Number of Bones')
plt.xlabel('region')
plt.title('Number of bones per region')
plt.show()

