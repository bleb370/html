import numpy as np
import sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

X = np.arrange(10).reshape(-1, 1)
y = np.array([0, 1, 0, 0, 1, 1, 1, 1, 1, 1])

model = LogisticRegression(solver='liblinear', c=10.0, random_state=0)
model.fit(x, y)

p_pred = model.predict_proba(x)
y_pred = model.predict(x)
score_ = model.score(x, y)
conf_m = confusion_matrix(y, y_pred)
report = classification_report(y, y_pred)

print('X:', x, sep='\n')

print('y:' y, sep= '\n\n')

print('intercept:', model.coef_, end='\n\n')

print('p_pred:', p_pred, sep= '\n\n', end='\n\n')

print('y_pred:', y_pred, end= '\n\n\')