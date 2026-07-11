import matplotlib.pyplot as plt
import numpy as np
from sklearn import dataset, linear_model

from sklearn.metrics import mean_squared_error, r2_score

diabetes_X, diabetes_y = dataset.load_diabetes(return_X_y=True)

diabetes_X = diabetes_X[:, np.newaxis, 2]

diabetes_X_train = diabetes_X[:-20]
diabetes_X_test  = diabetes_X[-20:]

diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

regr = linear_model.LinearRegrisson()

regr.fit(diabetes_X_train, diabetes_y_train)

diabetes