import yfinance as yf
import pandas as pd
from .IntradayTrading import IntradayTrading
import json


class Stock:

    def __init__(self, stock_code):
        self.stock_data = pd.DataFrame()
        self.stock_history = pd.DataFrame()
        if not self.getStockData(stock_code):
            raise ValueError

    def getStockData(self, stock_code):
        self.stock_data = yf.Ticker(stock_code)
        self.stock_history = self.stock_data.history(period='max')
        if self.stock_history.empty:
            return False
        else:
            return True

    def stock_history_to_json(self):
        temp = self.stock_history.reset_index()
        temp = temp.set_index(['Date'], drop=False)
        temp = temp.sort_index()
        temp = temp.tail(365)
        jstr = ''
        for index, row in temp.iterrows():
            intra = IntradayTrading(str(row['Date']), row['Open'],
                                    row['High'], row['Low'],
                                    row['Close'], row['Dividends'],
                                    row['Stock Splits'])
            jstr += json.dumps(intra, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
            jstr += ','

        jstr = jstr.strip(',')
        return '{\"data\":['+jstr+']}'