import pandas as pd


def find_moscow(x):
    if x[0].find("МОСКВА") > -1:
        return [x[0], x[1]*5]
    else:
        return x

data = pd.read_csv("https://video.ittensive.com/python-advanced/internet-2017.csv",
                   na_values="NA", names=["Регион", "2017"], decimal=",", skiprows=1)
data.fillna(0, axis=1, inplace=True)
data = data.apply(find_moscow, axis=1, result_type="expand")
print(data)
