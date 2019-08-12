from stock.models import Ticker
from stock.Stock import Stock
from stock.time_limited import time_limit


def init():
    codes = ['AAPL', 'BABA', 'GOOG', 'MSFT', 'EBAY', 'AMZN', 'INTC', 'NOK']

    for code in codes:
        print('---------------------------------------')
        print(code)
        stock_data = []
        stock = None
        try:
            stock = Stock(code)
        except ValueError:
            print("Illegal value: " + code)

        if stock:
            download(stock, stock_data)
            obj = None
            try:
                obj = Ticker.objects.get(pk=code)

                obj.stock_info = stock_data[0]
                obj.stock_history = stock_data[1]
                obj.stock_actions = stock_data[2]
                obj.stock_financials = stock_data[3]
                obj.stock_cashflow = stock_data[4]
                obj.stock_options = stock_data[5]
                obj.stock_balance_sheet = stock_data[6]
                obj.save()
            except Ticker.DoesNotExist:
                obj = Ticker.objects.create(stock_ticker=code,
                                            stock_info=stock_data[0],
                                            stock_history=stock_data[1],
                                            stock_actions=stock_data[2],
                                            stock_financials=stock_data[3],
                                            stock_cashflow=stock_data[4],
                                            stock_options=stock_data[5],
                                            stock_balance_sheet=stock_data[6])
                obj.save()
        print('---------------------------------------')


'''
    stock_ticker = models.CharField(primary_key=True, blank=False, unique=True, max_length=200)
    stock_info = models.TextField()
    stock_history = models.TextField()
    stock_actions = models.TextField()
    stock_financials = models.TextField()
    stock_cashflow = models.TextField()
    stock_options = models.TextField()
    stock_balance_sheet = models.TextField()
'''


def download(stock, stock_data):
    try:
        with time_limit(10):
            stock_data.append(stock.stock_info_to_json())
            print('stock_info Done')
    except Exception:
        stock_data.append('')
        print('stock_info Timeout')

    try:
        with time_limit(100):
            stock_data.append(stock.stock_history_to_json())
            print('stock_history Done')
    except Exception:
        stock_data.append('')
        print('stock_history Timeout')

    try:
        with time_limit(10):
            stock_data.append(stock.stock_actions_to_json())
            print('stock_actions Done')
    except Exception:
        stock_data.append('')
        print('stock_actions Timeout')

    try:
        with time_limit(10):
            stock_data.append(stock.stock_financials_to_json())
            print('stock_financials Done')
    except Exception:
        stock_data.append('')
        print('stock_financials Timeout')

    try:
        with time_limit(10):
            stock_data.append(stock.stock_cashflow_to_json())
            print('stock_cashflow Done')
    except Exception:
        stock_data.append('')
        print('stock_cashflow Timeout')

    try:
        with time_limit(10):
            stock_data.append(stock.stock_options_to_json())
            print('stock_options Done')
    except Exception:
        stock_data.append('')
        print('stock_options Timeout')

    try:
        with time_limit(10):
            stock_data.append(stock.stock_balance_sheet_to_json())
            print('stock_balance_sheet Done')
    except Exception:
        stock_data.append('')
        print('stock_balance_sheet Timeout')
