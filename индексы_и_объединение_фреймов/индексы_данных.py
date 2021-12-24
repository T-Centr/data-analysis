import pandas as pd


data = pd.read_csv("https://video.ittensive.com/python-advanced/internet-2017.csv",
                   na_values="NA", decimal=",", skiprows=1,
                   names=["Регион", "2017"], index_col="Регион")
data.fillna(0, axis=1, inplace=True)
data.index.name = "РЕГИОН"
data = data.reset_index()
print(data)
