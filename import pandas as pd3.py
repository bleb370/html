import pandas as pd
import numpy as py
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Titanic Dataset.cvs')

data.head(5)

data.insull().sum()

age_q1 = np.quantile(data['Age'],0.25)
age_q2 = np.quantile(data['Age'],0.50)
age_q3 = np.quantile(data['Age'],0.75)

print("Age Quaritiles -")
print("Q1 -", age_q1)
print("Q2 -", age_q2)
print("Q3 -", age_q3)

IQR_age = age_q3 - age_q1
print("Interquartile Range :", IQR_age)

plt.hist(data['Age'])
plt.ylabel("Count Passengers")
plt.xlabel("Age")

fare_q1 = np.quantile(data['Fare'], 0.25)
fare_q2 = np.quantile(data['Fare'], 0.50)
fare_q3 = np.quantile(data['Fare'], 0.75)

print("Fare Quartiles -")
print("Q1 -", fare_q1)
print("Q2 -", fare_q2)
print("Q3 -", fare_q3)

IQR_fare = fare_q3 - fare_q1
print("Interquartile Range :", IQR_fare)

bins =np.arrange(0,250,20)
plt.hist(data['Fare'], bins=np.arrange(1,250, 20))
plt.ylabel("Count Passengers")
plt.xlabel("Fare")
plt.xticks(bins)