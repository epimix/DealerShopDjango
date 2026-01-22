from django.contrib import admin
from django.urls import path
from . import views

app_name = 'bought'

urlpatterns = [
    path('', views.index, name='index'),
    path('buy/<int:car_id>/', views.buy_car, name='buy_car'),
]