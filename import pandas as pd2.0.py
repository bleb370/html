import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("heart.csv")

df.head()

df.shape

df.columns

df.describe()

df.insull().sum()

print(df.info())

df.hist(figsize=(12,12), laylout=(5,3))

df.plot(kind='box')