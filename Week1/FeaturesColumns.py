import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
ms = pd.DataFrame.from_csv('../data/microsoft.csv')

# Create PriceDiff in the DataFrame ms
ms['PriceDiff'] = ms['Close'].shift(-1) - ms['Close'] 

# Display the price difference of Microsoft on 2015-01-05
print(ms['PriceDiff'].loc['2015-01-05'])

# Create a new column Return in the DataFrame MS
ms['Return'] = ms['PriceDiff'] / ms['Close'] 

# Print the return on 2015-01-05
print(ms['Return'].loc['2015-01-05'])

# Create a new column Direction for MS
ms['Direction'] = [1 if ms['PriceDiff'].loc[ei] > 0 else 0 for ei in ms.index] 

# Show the price difference on 2015-01-05
print('Price difference on {} is {}. direction is {}'.format('2015-01-05', ms['PriceDiff'].loc['2015-01-05'], ms['Direction'].loc['2015-01-05']))

# You can use .rolling() to calculate any numbers of days' Moving Average. This is your turn to calculate "60 days"
# Moving average of Microsoft, rename it as "ma60". And follow the codes above in plotting a graph

ms['ma60'] = ms['Close'].rolling(60).mean() 

#plot the moving average
plt.figure(figsize=(10, 8))
ms['ma60'].loc['2015-01-01':'2015-12-31'].plot(label='MA60')
ms['Close'].loc['2015-01-01':'2015-12-31'].plot(label='Close')
plt.legend()
plt.show()
