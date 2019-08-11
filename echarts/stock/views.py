from django.shortcuts import render
from django.http import HttpResponse
from . import Stock
from .models import Ticker
from .models import User
from django.db import models
from django.shortcuts import redirect
from django.shortcuts import HttpResponse

# Create your views here.

def login(request):
    # request这是前端请求发来的请求，携带的所有数据，django给我们做了一些列的处理，封装成一个对象传过来
    if request.method == 'GET':
        return render(request,'stock/login.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        user_obj = User.objects.filter(name=name, pwd=pwd).first()
        if user_obj:
            return redirect('index/')
        else:
            return HttpResponse('用户名或密码错误')


def register(request):
    if request.method == 'GET':
        return render(request,'stock/register.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        re_pwd = request.POST.get('re_pwd')
        if name and pwd and re_pwd:
            if pwd == re_pwd:
                user_obj = User.objects.filter(name=name).first()
                if user_obj:
                    return HttpResponse('用户已存在')
                else:
                    User.objects.create(name=name,pwd=pwd).save()
                    return redirect('login/')
            else:
                return HttpResponse('两次密码不一致')

        else:
            return HttpResponse('不能有空！')




def stock_history(request):
    code = request.GET['code']
    code = str(code).upper()

    ticker = Ticker.objects.get(pk=code)
    return HttpResponse(ticker.stock_history)
    '''stock_his = None
    try:
        stock = Stock.Stock(code)
        stock_his = stock.stock_history_to_json()
    except ValueError:
        print("Illegal value.")
    return HttpResponse(stock_his)
    '''

def index(request):
    return render(request, 'stock/index.html')


