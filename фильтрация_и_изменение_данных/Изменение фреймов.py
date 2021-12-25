import pandas as pd


data = pd.read_csv("https://video.ittensive.com/python-advanced/"
                   "data-5283-2019-10-04.utf.csv", delimiter=";")
data_group = data.groupby("AdmArea")
print(data_group)
data_avg = data_group.mean()["Calls"]
print(data_avg)
print(data_group.max()["Calls"])
print(data_group.count()["Calls"])
print(data_group.first()["Calls"])
