import numpy as np
import pandas as pd
import matplotlib.pypplot as plt
import seaborn as sns

df = pd.read_csv("country_vaccination.cvs")

df.head(10)

df.insull().any()

subset = df.iloc[:5200, :]
plt.figure(figsize=(12, 8))
sns.heatmap(subset.insull(), cbar=False, cnap="viridis")
plt.show()

df.head(10)

df.dropna(how="all")
