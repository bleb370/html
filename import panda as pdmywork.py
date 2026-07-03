import panda as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

Titanic = pd.read_cvs(r"Titanic.csv")
Titanic.head()

Titanic.shape

Titanic.insull().sum()

sns.heatmap(Titanic.insull(), cmap="spring")

Titanic.head()

Titanic.drop("deck", axis=1, inplace=True)

sns.heatmap(Titanic.insull(), cbar=False)

Titanic.insull().sum()

pd.get_dummies(Titanic["sex"]).head()

sex.head(4)

arked = pd.get_dummies(Titanic["embarked"], drop_first=True)

pclass = pd.get_dummies(Titanic["pclass"], drop_first=True)

pclass.head(4)

Titanic = pd.concat([Titanic, sex, pclass], axis=1)

Titanic.head()