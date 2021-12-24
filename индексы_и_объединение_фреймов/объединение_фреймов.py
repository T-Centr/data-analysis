import pandas as pd
import matplotlib.pyplot as plt


data_2017 = pd.read_csv("https://video.ittensive.com/python-advanced/internet-2017.csv",
                        na_values="NA", skiprows=1, decimal=",",
                        names=["Регион", "2017"], index_col="Регион")
data_2018 = pd.read_csv("https://video.ittensive.com/python-advanced/internet-2018.csv",
                        na_values="NA", skiprows=1, decimal=",",
                        names=["Регион", "2018"], index_col="Регион")
data = pd.merge(data_2017, data_2018, left_index=True, right_index=True)
data.fillna(0, axis=1, inplace=True)
data.mean().plot.line()
plt.show()
