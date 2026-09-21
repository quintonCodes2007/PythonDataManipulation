import os
os.system('cls')
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv('male-elephant-tusk-size.csv')
#print(df.head(10))

# creating a pre proaching dataframe to see the tusk lenght

pre_poaching = df.query('period == "1966-68"')
#print(pre_poaching.head(3))


# do same for post poaching
post_recovery = df.query('period == "2005-13"')

#print(post_recovery.head(3))

# printing the avarage for before and after 

#print('Before: ', pre_poaching['tusk_length'].mean())
#print('After: ', post_recovery['tusk_length'].mean())

#ploting a scatter plot for tusk length and a shoulder and formating the plot
# plt.figure(figsize=(6, 4))
# plt.scatter(pre_poaching['shoulder_height'],
#             pre_poaching['tusk_length'], marker='^')
# plt.scatter(post_recovery['shoulder_height'], post_recovery['tusk_length'], marker='s')
# plt.xlabel('Shoulder height (cm)')
# plt.ylabel('Tusk Length (cm)')
# plt.text(x=200, y=120, s='Pre-poaching', color='C0')
# plt.text(x=200, y=35, s='Pre-poaching', color='C1')
# plt.show()

#modelling tusk length

# A linear model fits a straight line through the data
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

class LinearModel:
    def __init__(self, model_name=""):
        self.model_name = model_name
        
    def fit(self, x, y):
        x = pd.DataFrame(x)
        linear_model = LinearRegression().fit(x, y)
        y_pred = linear_model.predict(x)
        self.slope = linear_model.coef_[0]
        self.intercept = linear_model.intercept_
        self.rsquared = r2_score(y, y_pred)
        
    def predict(self, x):
        return self.slope * x + self.intercept

    def plot_model(self, x_min, x_max, color="black"):
        y_min = self.predict(x_min)
        y_max = self.predict(x_max)
        plt.plot([x_min, x_max], [y_min, y_max], color=color)
        
    def print_model_info(self):
        m = self.slope
        b = self.intercept
        rsquared = self.rsquared
        model_name = self.model_name
        print(f'LinearModel({model_name}):')
        print(f'Parameters: slope = {m:.2f}, intercept = {b:.2f}')
        print(f'Equation: y = {m:.2f}x + {b:.2f}')
        print(f'Goodness of Fit (R²): {rsquared:.3f}')

# creating linear model objects for both post and pre poaching data.
pre_model = LinearModel("pre_poaching")
pre_model.fit(x=pre_poaching['shoulder_height'], y=pre_poaching['tusk_length'])
post_model = LinearModel("post_recovery")
post_model.fit(x=post_recovery['shoulder_height'], y=post_recovery['tusk_length'])


plt.scatter(pre_poaching['shoulder_height'], pre_poaching['tusk_length'], marker='^')
plt.scatter(post_recovery['shoulder_height'], post_recovery['tusk_length'], marker='s')
plt.xlabel('Shoulder height (cm)')
plt.ylabel('Tusk length (cm)')
plt.text(200, 120, 'Pre-poaching', color='C0')
plt.text(220, 35, 'post_recovery', color='C1')
pre_model.plot_model(140, 250, 'C0')
post_model.plot_model(140, 250, 'C1')
plt.show()

pre_model.print_model_info()
post_model.print_model_info()




