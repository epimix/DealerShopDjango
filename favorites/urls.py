from django.contrib import admin
from django.urls import path
import favorites.views

app_name = 'favorites'

urlpatterns = [
    path('', favorites.views.index, name='index'),
    path('add/<int:car_id>/<str:return_url>/', favorites.views.add_car, name='add_car'),
    path('remove/<int:car_id>/<str:return_url>/', favorites.views.remove_car, name='remove_car'),
]