import matplotlib.pyplot as plt
import pandas as pd

# plotting a simple zig-zag pattern
# x and y are actual cordinates and not ranges so first point is a (1,3) and we use the plt.plot(x,y) function to plot and plt.show to display the graph and color= 'orange' is the color of the grapgh
# x = [1,2,3,4,5,6,7]
# y = [3,4,3,4,3,8,1]
# plt.plot(x, y, color='orange')
# plt.show()
# hello
# plotting a bar graph
# x = ['A','B','C']
# y = [200, 400, 600]
# plt.bar(x,y, color='red')
# plt.show()

# ploting a scatter plot
x = [1,2,3,4,5,6,7,8,9]
y = [1,2,3,3,5,6,7,7,9]

plt.scatter(x,y)
plt.show()

# using dataframes in .csv files to plot.
df = pd.read_csv('practice.csv')
print(df)
# 
# x = df['name']
# y = df['age']
# plt.bar(x,y)
# plt.show()

# this is how to plot with a single line of code using the df
plt.bar(df['name'],df['age'])
plt.title('Names and ages')
plt.ylabel('Ages')
plt.xlabel('Names')
plt.show()