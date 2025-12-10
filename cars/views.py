from django.shortcuts import render
from django.urls import reverse


cars = [
    {"id": 1, "brand": "Toyota", "model": "Camry", "year": 2020, "price": 24000},
    {"id": 2, "brand": "Honda", "model": "Accord", "year": 2019, "price": 22000},
    {"id": 3, "brand": "Ford", "model": "Mustang", "year": 2021, "price": 26000},
    {"id": 4, "brand": "Chevrolet", "model": "Malibu", "year": 2018, "price": 21000},
    {"id": 5, "brand": "Nissan", "model": "Altima", "year": 2022, "price": 25000},
]

def carsList(request):
    return render(request, "cars/list.html",{"cars": cars})

def carDetail(request, car_id):
    return render(request, "cars/detail.html", {"car": cars[car_id - 1]})


