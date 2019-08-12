from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'stock_history/', views.stock_history, name='stock_history'),
    path('', views.index, name='index'),
    re_path(r'GetStockInfo', views.test, name = 'test')
]