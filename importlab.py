
import pandas as pd
import numpy as np
import seaborn as sns

data = sns.load_dataset('iris')

data_q1 = np.quantile(data['petal_length'], 0.25)
data_q2 = np.quantile(data['petal_length'], 0.50)
data_q3 = np.quantile(data['petal_length'], 0.75)

print("First Quartile (Q1) -", data_q1)
print("Second Quartile (Q2) -", data_q2)
print("Third Quartile (Q3) -", data_q3)