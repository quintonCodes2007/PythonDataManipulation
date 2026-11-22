import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

from other_classes.py import LinearModel 

BASE_DIR = Path(__file__).resolve().parent

csv_path = BASE_DIR / "lion-attacks-lunar-cycle.csv"

df = pd.read_csv(csv_path)
#print(df.head())

plt.scatter(df['evening_moonlight'], df['attacks'], alpha=0.5)
plt.xlabel('Evening Moonlight')
plt.ylabel('Number of Lion Attacks')
#plt.show()


attack_model = LinearModel("attacks")
attack_model.fit(x=df['evening_moonlight'], y=df['attacks'])

plt.scatter(df['evening_moonlight'], df['attacks'], alpha=0.5)
plt.xlabel('Evening Moonlight')
plt.ylabel('Number of Lion Attacks')
attack_model.plot_model(0, 1)
plt.show()