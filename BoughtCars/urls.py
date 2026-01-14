from django.contrib import admin
from django.urls import path
import BoughtCars.views

urlpatterns = [
    path('', BoughtCars.views.index, name='index')
]