import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

from scipy import stats

# For file name reading
from os import listdir

x_name = "Temperature"
y_name = "Mortality"

plots = input("Plot graphs? (y/N)") == "y"

data1 = pd.read_csv("refined-data/deaths-and-accidents.csv")
y = data1["deaths"]
data2 = pd.DataFrame()

values = pd.DataFrame()

for file in listdir("refined-data/fuel-and-temperature"):
  city_name = file[:file.rfind(".csv")]
  data2 = pd.read_csv("refined-data/fuel-and-temperature/" + file)
  x = data2["temperature"]

  # Correlation with scipy
  r, p = stats.pearsonr(x, y)
  # print("Correlation for", city_name)
  # print("r-value:", r, "\np-value:", p)
  values = values.append(pd.DataFrame({"City": city_name, "r-value": [r], "p-value": [p]}))

  # Creating the scatter plot
  if plots:
    plt.scatter(x, y)
    plt.title("Correlation between " + x_name + " and " + y_name + " for " + city_name)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color="red")
    plt.show()

# values = values.append(pd.DataFrame({"City": "---AVERAGE---", "r-value": [values["r-value"].mean()], "p-value": [values["p-value"].mean()]}))
print(values.to_string(index = False))
