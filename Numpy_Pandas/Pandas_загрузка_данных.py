import pandas as pd


data = pd.read_csv('https://video.ittensive.com/python-advanced/'
                   'internet-2017.csv')
print(data.head())
print()


data = pd.read_csv('https://video.ittensive.com/python-advanced/'
                   'internet-2017.csv', na_values='NA', decimal=',')
data.fillna(0, axis=1, inplace=True)
data_array = data.values
print(data_array)
