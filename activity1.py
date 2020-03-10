import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io
import requests
from datetime import datetime

def main():

    # Read in data
    url='https://www.nasdaq.com/api/v1/historical/SBUX/stocks/2016-01-28/2020-02-28'
    s=requests.get(url).content
    stocks=pd.read_csv(io.StringIO(s.decode('utf-8')))
    stocks = stocks.iloc[::-1]

    # Formatting into correct objects
    for col in [' Close/Last', ' Open', ' High', ' Low']:
        stocks[col] = stocks[col].apply(lambda x: float(x[2:]))
    stocks['Date'] = stocks['Date'].apply(lambda x: datetime.strftime(datetime.strptime(x, '%m/%d/%Y'), '%b %d %Y'))
    stocks = stocks.rename(columns={' Close/Last': 'Close/Last', ' Open': 'Open', ' High': 'High', ' Low': 'Low'})

    # Basic Plot
    basicPlot(stocks)

    coolPlot(stocks)

    plt.show()

# Plots a basic plot that is
# not nice to look at
def basicPlot(stocks):
    plt.plot(stocks['Date'], stocks['High'])


# Plots a nice looking plot that 
# is far better to look at
def coolPlot(stocks):
    fig = plt.figure()

    ax = fig.add_subplot(111)

    ax.plot(stocks['Date'], stocks['High'])

    plt.xlabel('Date')
    plt.ylabel('High')
    plt.title('Starbucks Stocks over Time')

    plt.xticks(np.arange(0, len(stocks['High']), step=len(stocks['High']) // 4))

    for axis in ['top', 'right']:
        ax.spines[axis].set_visible(False)

    ax.yaxis.tick_left()
    ax.xaxis.tick_bottom()


if __name__ == "__main__":
    main()

"""
https://stackoverflow.com/questions/43326680/what-are-the-differences-between-add-axes-and-add-subplot

"""