import pandas as pd


data = pd.read_csv(
    "https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv",
    delimiter=";"
)
data["Percent"] = data.apply(
    lambda x: 100*x['UnemployedDisabled'] / x['UnemployedTotal'], axis=1)
data = data[data["Percent"] < 2]
data = data.set_index("Year")
data = data.sort_index()
print(data.index[0:1])
