import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('https://video.ittensive.com/python-advanced/'
                   'data-5283-2019-10-04.utf.csv', delimiter=';')
data['Month'] = data['Month'].str.upper().str.slice(0, 3).astype('category')
data_group = data.groupby('Month').mean()
print(data_group)
data_group = data_group.sort_values('Calls', ascending=True)
data_group['Calls'].plot.bar()
plt.show()
