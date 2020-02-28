import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io
import requests

url='https://www.nasdaq.com/api/v1/historical/SBUX/stocks/2020-01-28/2020-02-28'
s=requests.get(url).content
stocks=pd.read_csv(io.StringIO(s.decode('utf-8')))

print(stocks.columns)
for col in [' Close/Last', ' Open', ' High', ' Low']:
    stocks[col] = stocks[col].apply(lambda x: float(x[2:]))

# sns.lineplot(x='Date', y=' High', data=stocks)

plt.plot(stocks['Date'], stocks[' High'])
plt.show()
