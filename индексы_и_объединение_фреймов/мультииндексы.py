import pandas as pd


data = pd.read_csv("https://video.ittensive.com/python-advanced/internet-2017.csv",
                   na_values="NA", decimal=",", names=["Регион", "2017"], skiprows=1)

area_indexes = data[data["Регион"].str.contains("округ")].index
data_areas_index = [(lambda n: "AREA" if n in area_indexes else "REGION")(i)
                    for i in range(0, len(data.index))]

data["Тип"] = data_areas_index
data = data.set_index(["Тип", "Регион"])
data = data.sort_index()
areas = data.loc["AREA"]
print(areas)
