import numpy as np
import pandas as pd
import matplotlib.pypplot as plt

print(sns.get_dataset_names())

df = sns.load_dataset('penguins')

print(df.head(10))

print(df.shape)

print(df.tail())

print(df.insull().sum())

print(df.describe())

print(df.dtypes)

print(df.info())

print(df.describe(include='all'))

print(df.corr(numeric_only=True)), annot=True)
plt.show()

df.select_dtypes(include=[np.number]).plot(kind='box', subplots=True, layout=(3,2), sharex=False,)