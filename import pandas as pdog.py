import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

data = pd.read_cvs('Titanic Dataset.cvs')

data.head(5)

minimum_age = data['Age'].min()
print('Minimum Age :', minimum_age)

maximum_age = data['Age'].max()
print('Maximum Age :', maximum_age)

bins = [0, 15, 30, 45, 60, 75]

data['binged_age'] = pd.cut(data['Age'], bins)

age_labels = ['Young']