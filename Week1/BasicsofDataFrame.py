#import the packages "Pandas" and "MatPlotLib" into Jupyter Notebook
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
ms = pd.DataFrame.from_csv('../data/microsoft.csv')

# print head of ms, 1 line
print(ms.head())

# print the shape of ms, 1 line
print(ms.shape)

# print summary statistics of Microsoft
print(ms.describe())

# select all the price information of Microsoft in 2016.
ms_2016 = ms.loc['2016-01-01' : '2016-12-31']

# print the price of Microsoft on '2016-03-16'
print(ms_2016.loc['2016-03-16'])

# print the opening price of the last row
print(ms.iloc[-1,0])

plt.figure(figsize=(10, 8))
# plot only the Close price of 2016 of Microsoft, 1 line 
ms_2016['Close'].plot()
plt.show()
