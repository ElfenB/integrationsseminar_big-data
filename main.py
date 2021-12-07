import pandas as pd

# from pandas.tools import plotting
import numpy as np
import matplotlib.pyplot as plt

from scipy import stats
from scipy.stats import linregress

data = pd.read_csv("2020-12-06-prices.csv", sep=",")
data = data[data["e5change"] == 1]
data = data[data["e10change"] == 1]
x = data["e5"]
y = data["e10"]

b, a, r, p, std = linregress(x, y)
print('b: ' + str(b), '\na: ' + str(a), '\nr: ' + str(r), '\np: ' + str(p), '\nstd: ' + str(std))

# Correlation with numpy
print("Correlation with numpy")
print(np.corrcoef(x, y)[0][1])

# Correlation with scipy
print("Correlation with scipy")
print(stats.pearsonr(x, y))


plt.scatter(x, y)
plt.title("Correlation between e5 and e10 prices")
plt.xlabel("e5")
plt.ylabel("e10")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color="red")
plt.show()