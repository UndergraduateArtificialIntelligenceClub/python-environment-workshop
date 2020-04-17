from plots import Plot
import pandas as pd
from datetime import datetime

def main():

    plotter = Plot()

    # Read in data
    stocks=pd.read_csv("SBUX_Stocks.csv")
    stocks = stocks.iloc[::-1]

    # Formatting into correct objects
    for col in [' Close/Last', ' Open', ' High', ' Low']:
        stocks[col] = stocks[col].apply(lambda x: float(x[2:]))
    stocks['Date'] = stocks['Date'].apply(lambda x: datetime.strftime(datetime.strptime(x, '%m/%d/%Y'), '%b %d %Y'))

    stocks = stocks.rename(columns={' Close/Last': 'Close/Last', 
                                    ' Open': 'Open', 
                                    ' High': 'High', 
                                    ' Low': 'Low'})

    plotter.basicPlot(stocks, 'Date', 'High')
    # plotter.coolPlot(stocks, 'Date', 'High', 'Starbucks Stocks over Time')


if __name__ == "__main__":
    main()

"""
https://stackoverflow.com/questions/43326680/what-are-the-differences-between-add-axes-and-add-subplot

"""
