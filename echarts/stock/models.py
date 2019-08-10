from django.db import models


# Create your models here.
class Ticker(models.Model):
    stock_ticker = models.CharField(primary_key=True, blank=False, unique=True, max_length=200)
    stock_info = models.TextField()
    stock_history = models.TextField()
    stock_actions = models.TextField()
    stock_financials = models.TextField()
    stock_cashflow = models.TextField()
    stock_options = models.TextField()
    stock_balance_sheet = models.TextField()