import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


data = pd.read_csv("https://video.ittensive.com/python-advanced/"
                   "data-5283-2019-10-04.utf.csv", delimiter=";")
data_avg = data.groupby("Year").mean()
x = np.array(data_avg.index).reshape(len(data_avg.index), 1)
y = np.array(data_avg["Calls"]).reshape(len(data_avg.index), 1)
model = LinearRegression()
model.fit(x, y)
plt.scatter(x, y, color="orange")
x = np.append(x, [2020]).reshape(len(data_avg.index)+1, 1)
plt.plot(x, model.predict(x), color="blue", linewidth=3)
plt.show()
print(model.predict(np.array(2020).reshape(1, 1)))
