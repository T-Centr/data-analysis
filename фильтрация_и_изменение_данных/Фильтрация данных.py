import pandas as pd


data = pd.read_csv("https://video.ittensive.com/python-advanced/internet-2017.csv",
                   na_values="NA", decimal=",", names=["Регион", "2017"],
                   skiprows=1, index_col="Регион")
data_more10 = data[data["2017"] > 10]
data_more10_less12 = data[(data["2017"] > 10) & (data["2017"] < 12)]
data_null = data[data["2017"].isnull()]
data_notnull = data.loc[data.any(axis=1)]
data_filled = data.loc[:, data.all()]
data_nonull = data.dropna()
print(data_nonull)
