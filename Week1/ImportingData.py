# import the package "Pandas" into Jupyter Notebook
import pandas as pd

# import the stock price of Microsoft (microsoft.csv), of which the CSV is located in the same folder, and rename the Dataframe in "ms"
ms = pd.DataFrame.from_csv('../data/microsoft.csv')

# run this cell to ensure Microsoft's stock data is imported
print(ms.iloc[0, 0])
