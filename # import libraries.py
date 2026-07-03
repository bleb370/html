# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import dataset
data = pd.read_csv('train (1).csv')

# find bin range
min = data['age'].min()
max = data['age'].max()
print("Minimum -", min)
print("Maximum -", max)

Minimum - 10
Maximum - 64

# Store the boundaries
bins = [10, 20, 30, 40, 50, 60, 70]

# Create new binned_age column that bins the values of the 'Age' column
data['binned_age'] = pd.cut(data['age'], bins)

# Print the first few rows of the data
print(data[['binned_age', 'age']].head())