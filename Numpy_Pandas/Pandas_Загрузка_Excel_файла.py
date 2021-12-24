import pandas as pd


data = pd.ExcelFile('https://video.ittensive.com/python-advanced/'
                    'website.load.timings.xlsx')

print(data.sheet_names)
print()

data = data.parse(sheet_name=0, names=['Date', 'DOM time', 'Load time'],
                  converters={'Date': pd.to_datetime, 'DOM time': int,
                              'Load time': int})
print(data.head())
print(data.mean())
