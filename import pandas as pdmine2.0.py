import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
upload = files.upload()

data = pd.read_cvs('Weather Dataset.cvs')

data.head(5)

data.info()

data.insull().sum()

mean_temp = np.mean(data['Temperature (c)'])
print("Mean Temperature is :", mean_temp)

var_temp = np.var(data['Temperature (c)'])
print("Variation of Temperature is :", var_temp)

standard_deviation_temp = np.std(data['Temperature (c)'])
print("Standard Deviation of Temperature is :", standard_deviation_temp)

for i in range(1, 13):
    month = data.loc[data["month"] == i]["Temperature (c)"]
    print("For month "+str(i))
    print("Mean temperature is" + str(np.mean(month)))
    print("standard deviation is" + str(np.std(month)))