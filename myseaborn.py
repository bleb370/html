import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset("iris")
g = sns.pairplot(iris)
plt.show()