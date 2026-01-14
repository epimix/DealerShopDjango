from django.shortcuts import render, redirect
from BoughtCars.bought import get_bought_cars
from django.urls import reverse
from cars.models import Car

def index(request):
    cars = Car.objects.all()
    bought = get_bought_cars(request)
    cars = [car for car in cars if car.id in bought]
    return render(request, 'bought/index.html', {'cars': cars})


