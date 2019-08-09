from django.shortcuts import render
from django.http import HttpResponse
from . import Stock


# Create your views here.
def stock_history(request):
    code = request.GET['code']
    stock_his = None
    try:
        stock = Stock.Stock(code)
        stock_his = stock.stock_history_to_json()
    except ValueError:
        print("Illegal value.")
    return HttpResponse(stock_his)


def index(request):
    return render(request, 'stock/index.html')
