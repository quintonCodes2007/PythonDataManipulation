import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent

csv_path = BASE_DIR / "lion-attacks-lunar-cycle.csv"

df = pd.read_csv(csv_path)
print(df.head())

plt.scatter(df['evening_moonlight'], df['attacks'], alpha=0.5)
plt.xlabel('Evening Moonlight')
plt.ylabel('Number of Lion Attacks')
plt.show()

