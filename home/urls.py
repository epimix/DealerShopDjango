from django.contrib import admin
from django.urls import path

import home.views

urlpatterns = [
    path('', home.views.home, name='home'),
   path('buy/', home.views.buy_service, name='buy_service'),
]