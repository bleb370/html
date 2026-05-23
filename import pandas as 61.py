import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

data = pd.read_cvs('Titanic Dataset.cvs')

data.head(5)

sns.set_style('whitegrid')

sns.countplot(x='Survived', data=data)

sns.countplot(x='Gender', hue='Survived', data=data)

sns.countplot('Survived', data=data, palette='winter')

sns.countplot(x='Gender', hue='Survived', data=data, palette='winter')

sns.countplot(x='Embarked', data=data)

sns.countplot(x='Embarked', data=data)
plt.xticks(rotation=30, frontsize=20)
plt.show()