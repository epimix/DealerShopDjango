from django.contrib import admin
from django.urls import path

import cars.views

urlpatterns = [
    path('',cars.views.car_index, name='car_index'),
    path('list', cars.views.carsList),
    path('<int:car_id>/', cars.views.carDetail, name='car_detail'),
    path('delete/<int:car_id>/', cars.views.deleteCar),
    path('edit/<int:car_id>/', cars.views.editCar),
    path('create/', cars.views.createCar),
]