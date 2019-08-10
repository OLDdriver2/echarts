import yfinance as yf
import pandas as pd
from stock.models import Ticker
from stock.Stock import Stock


def init():
    codes = ['AAPL', 'BABA', 'GOOG', 'MSFT', ' EBAY', 'AMZN', 'INTC', 'NOK']

    for code in codes:
        try:
            stock = Stock(code)
            stock_his = stock.stock_history_to_json()
            ticker = Ticker.objects.create(stock_ticker=code, stock_history=stock_his)
            ticker.save()
            print(code + ' Done')
        except ValueError:
            print("Illegal value.")
