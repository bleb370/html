import pandas as pd
import math
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:, :2]
Y = iris.target

logreg = MultiClassLogisticRegression()

logreg.fit(X, Y)

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

Z = Z.reshape(xx.shape)
plt.figure(1, figsize=(4, 3))
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)
plt.xlabel("Sepal lenght")
plt.ylabel("Sepal width")

plt.xlim(xx.min(), yy.max())
plt.ylim(xx.min(), yy.max())
plt.xticks(())
plt.yticks(())

plt.show()