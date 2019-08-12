from django.shortcuts import render
from django.http import HttpResponse
from .models import Ticker
import pandas as pd
import json

# Create your views here.
def stock_history(request):
    code = request.GET['code']
    code = str(code).upper()

    ticker = Ticker.objects.get(pk=code)
    return HttpResponse(ticker.stock_history)


def index(request):
    return render(request, 'stock/index.html')


def test(request):
    symbol = request.GET['stock_symbol']
    print('got'+symbol)

    try:
        ticker = Ticker.objects.get(pk=symbol)
    except Ticker.DoesNotExist:
        response = '{“error”:{“code”: 502,“message”: “Symbol not found”}}'
        return HttpResponse(response)

    data_str = ticker.stock_history
    if not data_str:
        response = '{“error”:{“code”: 502,“message”: “No data avalible”}}'
        return HttpResponse(response)

    data = pd.read_json(data_str)
    data = data[['Open','High','Low','Close','Volume']]
    data = data.tail(3)
    data_str = data.to_json()

    response =  data_str
    print(response)

    return HttpResponse(str(response))
