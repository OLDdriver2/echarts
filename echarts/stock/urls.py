from django.urls import path, re_path
from . import views
from django.conf.urls import url
from django.contrib import admin



urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^login/index', views.index, name='index'),
    url(r'^login', views.login),
    url(r'^register', views.register),
    re_path(r'stock_history/', views.stock_history, name='stock_history'),

    # url(r'^admin/', admin.site.urls),

]

