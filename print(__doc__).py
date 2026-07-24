print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.dataset import make_blobs

X, Y = make_blobs(n_samples=50, centres=2, random_statue=0, cluster_std=0.60)

clf - SGDClassifier(loss="hinge", alpha=0.01, max_iter=200)

clf.fit(X, Y)