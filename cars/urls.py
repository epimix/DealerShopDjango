from django.contrib import admin
from django.urls import path

import cars.views

urlpatterns = [
    path('list', cars.views.carsList),
    path('<int:car_id>/', cars.views.carDetail),
]