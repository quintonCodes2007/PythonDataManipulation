import pandas as pd
import matplotlib.pyplot as plt
from other_classes import LinearModel

df = pd.read_csv('lion-attacks-lunar-cycle.csv')
##print(df)

#plt.scatter(df['evening_moonlight'], df['attacks'], alpha=0.5)
#plt.xlabel('Evening Moonlight')
#plt.ylabel('Number of attacks')
#plt.show()

attack_model = LinearModel("attacks")
attack_model.fit(x=df['evening_moonlight'], y=df['attacks'])

plt.scatter(df['evening_moonlight'], df['attacks'], alpha=0.5)
plt.xlabel('Evening Moonlight')
plt.ylabel('Number of attacks')
attack_model.plot_model(0, 1)
plt.show()