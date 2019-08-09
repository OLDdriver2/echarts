
class IntradayTrading(object):
    def __init__(self, date, o, h, l, c, dividens, splits):
        self.Date = date
        self.Open = o
        self.High = h
        self.Low = l
        self.Close = c
        self.Dividends = dividens
        self.Splits = splits
